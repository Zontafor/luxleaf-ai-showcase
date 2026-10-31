# Development validation

## v0.3 integration increment

For the relationship between observed results, remaining uncertainty, and proposed release gates, read the [Product & Technical Brief](TECHNICAL_BRIEF.md).

Recorded October 30, 2026: **81 tests passed with SQLite and the same 81 with isolated PostgreSQL 14.20**. New checks cover tenant discovery and redacted model catalogs; JSON/legacy workflow compatibility and provider-disable replay; the private async client; MCP tool discovery, explicit workflow opt-in and cross-tenant denial; S3 SDK contracts, private-bucket preflight, conflicting-object refusal, uncertain-write recovery, independent receipts, concurrent delivery and archive opt-in; metadata-envelope validation and forward-schema rejection.

A backed-up local schema upgrade preserved the synthetic demonstration. The executable private discovery example and a local query/JSON workflow smoke run passed with zero recorded model cost. No live S3 or inference-provider call occurred. Remote archive retention, immutability, identity policies and deployment capacity are unverified. See [integration scope](INTEGRATIONS.md).

## v0.2 historical record

Recorded October 30, 2026 for the private LuxLeaf v0.2 development foundation.

| Area | Recorded result |
|---|---|
| Automated suite | 57 tests passed with SQLite; the same 57 tests passed with isolated PostgreSQL 14.20 |
| Authorization | Tenant separation, revoked/inactive access, admin/member permissions, and rejected tenant spoofing |
| Accounting | Budget reservations, rate limits, idempotent replay, concurrent admission, and uncertain-outcome reconciliation |
| Workflows | Submission, execution, cancellation, revoked submitter behavior, duplicate protection, and operator recovery |
| Model adapters | Synthetic HTTP or SDK contract checks for Azure, Bedrock, and Vertex; no live paid calls |
| MCP | In-memory protocol session checks for discovery, tenant boundaries, replay, validation, and revocation |
| Operational records | Transactional event rollback, crash replay, corrupt-file rejection, and concurrent export |
| Privacy checks | Synthetic secrets absent from application trace output and structured completion logs |
| Retrieval | Three artificial positive cases and one no-evidence case; other-tenant results remained empty |
| Local demonstration | Synthetic policy retrieval, completed workflows, recorded zero-cost local usage, and event export |

These results were observed on macOS arm64 with Python 3.14.3. They are maintainer-recorded development evidence; the private test suite and application source are not distributed here.

## What remains unverified

Live Azure/Bedrock/Vertex integration, Linux container runtime, deployed Kubernetes resources, external MCP-host integration, remote trace collection, load targets, backup restoration, production penetration testing, and regulatory compliance remain outside these results. A small synthetic retrieval evaluation does not establish model faithfulness or domain suitability.

## What public CI checks

The showcase workflow validates an explicit file allowlist, checks for prohibited paths and recognizable credential patterns, verifies local documentation links and image references, and checks SVG syntax. It cannot inspect the private application. A passing showcase check is not a security certification or proof that every possible sensitive value has been detected.
