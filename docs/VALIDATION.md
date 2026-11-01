# Development validation

## Connected demonstrations

Recorded October 30, 2026: five synthetic journeys executed 35 recorded steps across all 31 components and passed 29 executable checks. The local portfolio suite now passes 9 tests, including complete coverage, evidence-output privacy and a deliberate budget-bypass fault that must stop recording. The developer-kit component’s 4 existing tests and compilation of the new runner passed. The runner uses disposable databases and no network calls. Configuration assertions, approvals, metric samples, image identifiers and compute capacity are synthetic fixtures; the SQLite migration and backup check execute locally. [Inspect the demonstrations](DEMONSTRATIONS.md).

## Independent components 0.1.0

Recorded October 30, 2026 on macOS arm64 / Python 3.14.3: 129 component tests across 31 separate repositories, 6 portfolio integration tests, and 31 CLI examples passed. Each CLI also rejected invalid envelopes and excessive JSON nesting. Python lint/format checks, local documentation links and source artifact boundaries were checked. Integration tests cover authenticated retrieval through local inference, workflow completion, budget settlement, archive acknowledgement, model governance, local tools, concurrent reservations and rollback. All 31 component GitHub workflows subsequently passed on their exact uploaded commits. Private visibility, non-fork status and remote commit identity were verified for all 31 repositories. The six portfolio integration tests remain local evidence; each component workflow runs that repository’s own unit suite. No cloud or production deployment was performed.

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

## October 31: managed event delivery

The expanded independent portfolio passed 143 component tests, 12 integration tests and 31 CLI examples locally. The event package has 18 tests; the new event/archive recovery runner passes ten assertions, with separate negative tests that falsify replay and bypass stale-worker rejection. [Recovery evidence and architecture](demonstrations/event-delivery-recovery.md) describe the injected fault and local-only limits. Earlier records below or above remain historical snapshots.

## October 31: all-component expansion

All 31 packages now have checked expansion scenarios. The current source portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. Expansion scenarios passed 122 assertions. [Current evidence and exact commits](demonstrations/all-component-expansion.md) supersede earlier counts for the updated code; older records remain historical.

All 31 wheels were built from committed source and installed together into a fresh environment without network dependency resolution. Their 174 component tests passed against the installed packages. All 31 source archives include licenses, tests, examples and expansion architecture documents. Generated Compose health-check configuration passed local Docker Compose configuration validation; no container or cluster was started.

## October 31: durable coordinated knowledge

The current source portfolio passed 188 component tests, 23 integration tests and 31 CLI examples. Workflow has 20 package tests; the maintained cross-package coordinator suite has nine tests. Six actual subprocess interruption cases passed 54 assertions. [Read the exact fault model and evidence](demonstrations/coordinated-knowledge-recovery.md). This adds real process loss between separate local transactions; it does not establish power-loss durability, live-cloud acceptance or production throughput.

## October 31: full-system pipeline composition

The current portfolio passed 198 component tests, 28 cross-component integration tests and 31 CLI examples. Developer Kit 0.4.0 adds ten engine tests and five system integration tests. The [system evidence](demonstrations/system-pipeline-record.json) records 37 completed stages, all 31 clean component commits, 16 assertions and four downstream-blocking scenarios. [Architecture and limits](SYSTEM_ARCHITECTURE.md). Earlier records remain historical snapshots.
