"""Check the public showcase boundary using only Python's standard library."""
from pathlib import Path
import os
import json
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
# Explicitly reviewed public repositories; backend source remains outside this navigation boundary.
PUBLIC_REPOSITORIES = {
    "luxleaf-ai-showcase", "luxleaf-scene-kit", "luxleaf-glass-ui",
    "luxleaf-gradient-studio", "luxleaf-metal-mark",
}


def verify(root=ROOT):
    errors = []
    entries = (root / "PUBLIC_FILES.txt").read_text().splitlines()
    allowed = {line.strip() for line in entries if line.strip() and not line.startswith("#")}
    if any(Path(name).is_absolute() or ".." in Path(name).parts for name in allowed):
        errors.append("Allowlist contains a non-relative or traversing path")
    actual = set()
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in dirs + files:
            path = Path(directory) / name
            if path.is_symlink():
                errors.append(f"Symlink is not publishable: {path.relative_to(root)}")
        actual.update(str((Path(directory) / name).relative_to(root)) for name in files)
    for name in sorted(actual - allowed):
        errors.append(f"Unexpected file: {name}")
    for name in sorted(allowed - actual):
        errors.append(f"Missing allowlisted file: {name}")
    patterns = [
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
        re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
        re.compile(r"\bll_[A-Za-z0-9_-]{25,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    private_paths = ["/Volumes" + "/", "/Users" + "/", "/private" + "/tmp/", "file:" + "//"]
    markdown_links = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)')
    html_links = re.compile(r'(?:src|href)=["\']([^"\']+)["\']')
    for name in sorted(actual & allowed):
        path = root / name
        if path.is_symlink():
            continue
        if path.stat().st_size > 1_000_000:
            errors.append(f"Oversized showcase asset: {name}")
            continue
        if path.suffix == ".py" and name != "scripts/verify_showcase.py":
            errors.append(f"Application code is outside showcase scope: {name}")
        if path.suffix in {".jpg", ".jpeg"}:
            content = path.read_bytes()
            if not content.startswith(b"\xff\xd8\xff") or not content.endswith(b"\xff\xd9"):
                errors.append(f"Invalid JPEG asset: {name}")
            if any(marker in content for marker in (b"Exif\x00\x00", b"http://ns.adobe.com/xap/", b"Photoshop 3.0")):
                errors.append(f"JPEG metadata requires review: {name}")
            continue
        if path.suffix == ".png":
            content = path.read_bytes()
            if not content.startswith(b"\x89PNG\r\n\x1a\n"):
                errors.append(f"Invalid PNG asset: {name}")
            # Reject text/EXIF metadata as an extra public-asset boundary check.
            offset = 8
            while offset + 12 <= len(content):
                size = int.from_bytes(content[offset:offset + 4], "big")
                kind = content[offset + 4:offset + 8]
                if kind in {b"tEXt", b"iTXt", b"zTXt", b"eXIf"}:
                    errors.append(f"PNG metadata requires removal/review: {name}")
                offset += size + 12
            continue
        try:
            text = path.read_text()
        except UnicodeError:
            errors.append(f"Unexpected binary asset: {name}")
            continue
        if any(pattern.search(text) for pattern in patterns):
            errors.append(f"Recognizable credential pattern in {name}; value suppressed")
        if any(fragment in text for fragment in private_paths):
            errors.append(f"Private filesystem reference in {name}")
        if path.suffix == ".md":
            for target in markdown_links.findall(text) + html_links.findall(text):
                parsed = urlsplit(target)
                github_path = unquote(parsed.path).strip("/").split("/")
                if (
                    parsed.hostname == "github.com"
                    and len(github_path) >= 2
                    and github_path[0].lower() == "zontafor"
                    and github_path[1].lower() not in PUBLIC_REPOSITORIES
                ):
                    errors.append(f"Public navigation points outside the reviewed public repositories in {name}")
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                    errors.append(f"Broken or out-of-repository local link in {name}: {target}")
        if path.suffix == ".svg":
            try:
                tree = ET.fromstring(text)
                if any(element.tag.rsplit("}", 1)[-1] in {"script", "foreignObject"} for element in tree.iter()):
                    errors.append(f"Active SVG content is not permitted: {name}")
            except ET.ParseError:
                errors.append(f"Invalid SVG syntax: {name}")
    catalog_path = root / "docs/projects/catalog.json"
    if catalog_path.is_file():
        try:
            catalog = json.loads(catalog_path.read_text())
            pages = {entry["page"] for entry in catalog}
            names = {entry["name"] for entry in catalog}
            if len(catalog) != 31 or len(pages) != 31 or len(names) != 31:
                errors.append("Public project catalog must contain 31 distinct projects")
            for entry in catalog:
                page = entry["page"]
                if page not in allowed or not page.startswith("docs/projects/"):
                    errors.append("Project page is outside the reviewed public file set")
                if set(entry["example"]) != {"request", "result"}:
                    errors.append("Project catalog is missing a recorded request/result example")
        except (ValueError, KeyError, TypeError):
            errors.append("Invalid public project catalog")
    else:
        errors.append("Public project catalog is missing")
    demonstration_path = root / "docs/demonstrations/record.json"
    if demonstration_path.is_file():
        try:
            record_text = demonstration_path.read_text()
            record = json.loads(record_text)
            journeys = record["scenarios"]
            components = {row["name"] for row in json.loads(catalog_path.read_text())}
            observed = {step["component"] for journey in journeys for step in journey["steps"]}
            checks = [check for journey in journeys for check in journey["checks"]]
            if len(journeys) != 5 or observed != components or set(record["coverage"]) != components:
                errors.append("Connected demonstrations must cover all 31 components in five journeys")
            if record["checks_passed"] != len(checks) or not all(check["passed"] is True for check in checks):
                errors.append("Demonstration check totals or outcomes are inconsistent")
            if record["live_cloud_calls"] is not False or record["production_measurements"] is not False:
                errors.append("Demonstration evidence must retain its synthetic execution boundary")
            if any(value in record_text for value in (
                "demo-local-only", "Bearer ", "lease_token", "pseudonym_key", *private_paths
            )):
                errors.append("Private execution detail found in demonstration evidence")
            for journey in journeys:
                page = f"docs/demonstrations/{journey['id']}.md"
                if page not in allowed or not (root / page).is_file():
                    errors.append("Demonstration is missing its reviewed public page")
        except (ValueError, KeyError, TypeError):
            errors.append("Invalid connected demonstration record")
    else:
        errors.append("Connected demonstration record is missing")
    recovery_path = root / "docs/demonstrations/event-recovery-record.json"
    try:
        recovery_text = recovery_path.read_text()
        recovery = json.loads(recovery_text)
        if (
            recovery["scenario"] != "event-delivery-recovery"
            or recovery["synthetic"] is not True
            or recovery["live_cloud_calls"] is not False
            or recovery["production_measurements"] is not False
            or len(recovery["checks"]) != 10
            or recovery["checks_passed"] != 10
            or not all(check["passed"] is True for check in recovery["checks"])
            or set(recovery["component_worktrees_dirty"]) != {"luxleaf-events", "luxleaf-archives"}
            or any(value is not False for value in recovery["component_worktrees_dirty"].values())
            or recovery["archive"]["entries"] != 1
            or recovery["archive"]["valid"] is not True
            or recovery["recovery"]["archive_replayed"] is not True
            or recovery["final"]["counts"]["completed"] != 1
        ):
            errors.append("Recovery record has inconsistent outcomes or evidence boundaries")
        if any(value in recovery_text for value in (
            "lease_token", "token_hash", "Bearer ", *private_paths
        )):
            errors.append("Private execution detail found in recovery evidence")
    except (OSError, ValueError, KeyError, TypeError):
        errors.append("Missing or invalid recovery demonstration record")
    try:
        expansion_text = (root / "docs/demonstrations/expansion-record.json").read_text()
        expansion = json.loads(expansion_text)
        records = expansion["components"]
        expected = {row["name"] for row in json.loads(catalog_path.read_text())}
        names = {row["name"] for row in records}
        checks = [check for row in records for check in row["checks"]]
        if (
            len(records) != 31 or names != expected
            or expansion["scenario"] != "all-component-expansion"
            or expansion["synthetic"] is not True
            or expansion["live_cloud_calls"] is not False
            or expansion["production_measurements"] is not False
            or expansion["checks_passed"] != len(checks)
            or not all(check["passed"] is True for check in checks)
        ):
            errors.append("Expansion evidence has invalid coverage or outcomes")
        for row in records:
            page = f"docs/architectures/{row['name']}.md"
            if (
                page not in allowed or not (root / page).is_file()
                or row["worktree_dirty"] is not False or not row["checks"]
                or row["synthetic"] is not True or row["live_cloud_calls"] is not False
                or re.fullmatch(r"[0-9a-f]{40}", row["source_commit"]) is None
                or re.fullmatch(r"\d+\.\d+\.\d+", row["version"]) is None
            ):
                errors.append("Expansion component lacks reviewed architecture or clean source evidence")
        if any(value in expansion_text for value in (
            "lease_token", "token_hash", "pseudonym_key", "synthetic-token", "Bearer ", *private_paths
        )):
            errors.append("Private execution details in expansion evidence")
    except (OSError, ValueError, KeyError, TypeError):
        errors.append("Missing or invalid all-component expansion evidence")
    try:
        coordination_text = (root / "docs/demonstrations/coordinated-knowledge-record.json").read_text()
        coordination = json.loads(coordination_text)
        stages = ["reserve", "answer", "settle", "event", "archive", "acknowledge"]
        expected_repos = {f"luxleaf-{name}" for name in (
            "workflows", "workspace", "knowledge", "inference", "metering",
            "events", "archives", "developer-kit"
        )}
        cases = coordination["cases"]
        if (
            coordination["schema_version"] != 1
            or coordination["scenario"] != "coordinated-knowledge-process-recovery"
            or coordination["synthetic"] is not True
            or coordination["live_cloud_calls"] is not False
            or coordination["production_measurements"] is not False
            or coordination["real_process_termination"] is not True
            or coordination["checks_passed"] != 54
            or len(cases) != 6
            or {case["crash_after"] for case in cases} != set(stages)
            or set(coordination["components"]) != expected_repos
        ):
            errors.append("Coordinated recovery coverage or evidence boundary is invalid")
        for component in coordination["components"].values():
            if component["worktree_dirty"] is not False or re.fullmatch(r"[0-9a-f]{40}", component["commit"]) is None:
                errors.append("Coordinated recovery lacks clean source evidence")
        for case in cases:
            expected_attempts = {stage: 2 if stage == case["crash_after"] else 1 for stage in stages}
            if (
                case["exit_code"] != 73 or case["recovery_exit_code"] != 0
                or case["completed_steps"] != stages or case["attempts"] != expected_attempts
                or len(case["checks"]) != 9
                or not all(check["passed"] is True for check in case["checks"])
                or case["available_micros"] != 100 or case["archive_entries"] != 1
                or case["ledger_entries"] != 1 or case["citation_count"] != 2
            ):
                errors.append("Coordinated recovery case has inconsistent outcomes")
        if any(value in coordination_text for value in (
            "lease_token", "token_hash", "pseudonym_key", "Bearer ", *private_paths
        )):
            errors.append("Private execution details in coordinated recovery evidence")
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        errors.append("Missing or invalid coordinated recovery evidence")
    try:
        system_text = (root / "docs/demonstrations/system-pipeline-record.json").read_text()
        system = json.loads(system_text)
        architecture = system["architecture"]
        execution = system["execution"]
        expected = {row["name"] for row in json.loads(catalog_path.read_text())}
        if (
            system["schema_version"] != 1 or system["scenario"] != "system-pipeline-composition"
            or system["synthetic"] is not True or system["live_cloud_calls"] is not False
            or system["production_measurements"] is not False
            or set(system["components"]) != expected or set(architecture["components"]) != expected
            or len(architecture["pipelines"]) != 5 or len(architecture["stages"]) != 37
            or execution["status"] != "completed" or execution["completed"] != 37
            or execution["unstarted"] != [] or execution["automatic_retry"] is not False
            or execution["durable_resume"] is not False
            or execution["plan_sha256"] != architecture["plan_sha256"]
            or re.fullmatch(r"[0-9a-f]{64}", execution["plan_sha256"]) is None
            or re.fullmatch(r"[0-9a-f]{64}", execution["execution_sha256"]) is None
            or system["checks_passed"] != 16 or len(system["checks"]) != 16
            or not all(row["passed"] is True for row in system["checks"])
        ):
            errors.append("System pipeline evidence coverage or boundary is invalid")
        for source in system["components"].values():
            if source["worktree_dirty"] is not False or re.fullmatch(r"[0-9a-f]{40}", source["commit"]) is None:
                errors.append("System pipeline evidence lacks clean source commits")
        graph = architecture["stages"]
        receipts = execution["stages"]
        if len(receipts) != 37 or len({row["id"] for row in graph}) != 37:
            errors.append("System pipeline stage count is invalid")
        seen = set()
        for stage, receipt in zip(graph, receipts):
            if (
                set(receipt) != {"stage", "pipeline", "component", "mode", "status", "input_sha256", "output_sha256"}
                or receipt["stage"] != stage["id"] or receipt["status"] != "completed"
                or receipt["component"] != stage["component"] or stage["component"] not in expected
                or receipt["pipeline"] != stage["pipeline"] or stage["pipeline"] not in architecture["pipelines"]
                or receipt["mode"] != stage["mode"] or stage["mode"] not in {"local-operation", "proposal-only"}
                or not set(stage["dependencies"]) <= seen
                or any(re.fullmatch(r"[0-9a-f]{64}", receipt[key]) is None for key in ("input_sha256", "output_sha256"))
            ):
                errors.append("System pipeline receipt or dependency ordering is invalid")
            seen.add(stage["id"])
        if {stage["component"] for stage in graph} != expected:
            errors.append("System pipeline graph omits a component")
        negative = system["negative_cases"]
        expected_faults = {"service-denial": "agent-policy", "posture-failure": "posture", "release-gate-failure": "bundle", "image-binding-failure": "bundle"}
        if len(negative) != 4 or {row["fault"] for row in negative} != set(expected_faults):
            errors.append("System pipeline failure cases are incomplete")
        for row in negative:
            if row["stopped_at"] != expected_faults.get(row["fault"]) or row["deployment_unstarted"] is not True or row["status"] not in {"blocked", "uncertain"}:
                errors.append("System pipeline failure case does not stop downstream work")
        if any(value in system_text for value in ("lease_token", "token_hash", "pseudonym_key", "Bearer ", *private_paths)):
            errors.append("Private execution detail in system pipeline evidence")
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        errors.append("Missing or invalid system pipeline evidence")
    return errors, len(actual)


if __name__ == "__main__":
    findings, count = verify()
    if findings:
        print("Showcase verification failed:\n" + "\n".join(findings))
        sys.exit(1)
    print(f"PASS: {count} allowlisted files; publication boundary, local links, and assets checked.")
    print("This check does not scan the private platform or guarantee absence of every sensitive value.")
