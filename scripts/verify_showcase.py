"""Check the public showcase boundary using only Python's standard library."""
from pathlib import Path
import os
import json
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


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
                    and github_path[1].lower() != "luxleaf-ai-showcase"
                ):
                    errors.append(f"Public navigation points outside the public showcase in {name}")
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
    return errors, len(actual)


if __name__ == "__main__":
    findings, count = verify()
    if findings:
        print("Showcase verification failed:\n" + "\n".join(findings))
        sys.exit(1)
    print(f"PASS: {count} allowlisted files; publication boundary, local links, and assets checked.")
    print("This check does not scan the private platform or guarantee absence of every sensitive value.")
