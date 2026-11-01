# All-component expansion demonstrations

Next integration: [durable knowledge recovery across six real process interruptions](coordinated-knowledge-recovery.md).

[Architecture index](../PORTFOLIO_ARCHITECTURE.md) · [Earlier connected demonstrations](../DEMONSTRATIONS.md)

**31 of 31 components expanded · 122 executable assertions passed · October 31, 2026**

Every component now has a dedicated implementation addition, contract documentation, architecture diagram and checked synthetic scenario. These are local package expansions, not 31 newly deployed services. The source and installable package artifacts remain private.

## Browse the evidence

| Component architecture and evidence | Version | New behavior | Assertions |
|---|---|---|---|
| [luxleaf-workspace](../architectures/luxleaf-workspace.md) | 0.2.0 | Membership revisions and audit | 4 |
| [luxleaf-knowledge](../architectures/luxleaf-knowledge.md) | 0.2.0 | Document reader restrictions | 5 |
| [luxleaf-inference](../architectures/luxleaf-inference.md) | 0.2.0 | Exact output budgets and passage deduplication | 3 |
| [luxleaf-metering](../architectures/luxleaf-metering.md) | 0.2.0 | Reviewed unknown-usage reconciliation | 5 |
| [luxleaf-workflows](../architectures/luxleaf-workflows.md) | 0.2.0 | Active workflow lease renewal | 4 |
| [luxleaf-environments](../architectures/luxleaf-environments.md) | 0.2.0 | Contained nonoverlapping subnet plans | 4 |
| [luxleaf-evaluations](../architectures/luxleaf-evaluations.md) | 0.2.0 | Measured retrieval quality gates | 4 |
| [luxleaf-model-router](../architectures/luxleaf-model-router.md) | 0.2.0 | Latency-aware routing and fallback order | 4 |
| [luxleaf-generation](../architectures/luxleaf-generation.md) | 0.2.0 | Whole-record context budgeting | 5 |
| [luxleaf-agent-plans](../architectures/luxleaf-agent-plans.md) | 0.2.0 | Dependency waves and plan identity | 3 |
| [luxleaf-tool-protocol](../architectures/luxleaf-tool-protocol.md) | 0.2.0 | Bounded local tool batches | 3 |
| [luxleaf-cloud-tools](../architectures/luxleaf-cloud-tools.md) | 0.2.0 | Region constraints and unambiguous resource paths | 5 |
| [luxleaf-agent-runtime](../architectures/luxleaf-agent-runtime.md) | 0.2.0 | Dependency-order enforcement | 3 |
| [luxleaf-rag](../architectures/luxleaf-rag.md) | 0.2.0 | Distinct-source quorum before inference | 4 |
| [luxleaf-model-governance](../architectures/luxleaf-model-governance.md) | 0.2.0 | Approval freshness and revocation | 4 |
| [luxleaf-batch](../architectures/luxleaf-batch.md) | 0.2.0 | Exact placement selectors | 3 |
| [luxleaf-events](../architectures/luxleaf-events.md) | 0.3.0 | Managed event lease renewal | 5 |
| [luxleaf-rollouts](../architectures/luxleaf-rollouts.md) | 0.2.0 | Idempotent rollout observations | 4 |
| [luxleaf-runtime](../architectures/luxleaf-runtime.md) | 0.2.0 | HTTP readiness and liveness probes | 5 |
| [luxleaf-archives](../architectures/luxleaf-archives.md) | 0.2.0 | Verified archive pagination | 4 |
| [luxleaf-data](../architectures/luxleaf-data.md) | 0.2.0 | Read-only database inspection | 3 |
| [luxleaf-developer-kit](../architectures/luxleaf-developer-kit.md) | 0.2.0 | Transitive rebuild planning | 3 |
| [luxleaf-api](../architectures/luxleaf-api.md) | 0.2.0 | Credential expiry and route scopes | 4 |
| [luxleaf-service-policy](../architectures/luxleaf-service-policy.md) | 0.2.0 | Exact resource-scoped service rules | 4 |
| [luxleaf-security](../architectures/luxleaf-security.md) | 0.2.0 | Posture regression comparison | 3 |
| [luxleaf-telemetry](../architectures/luxleaf-telemetry.md) | 0.2.0 | Explicit pseudonym-key rotation | 4 |
| [luxleaf-observability](../architectures/luxleaf-observability.md) | 0.2.0 | Combined latency and availability objective | 4 |
| [luxleaf-incidents](../architectures/luxleaf-incidents.md) | 0.2.0 | Evidence-backed incident ownership handoff | 4 |
| [luxleaf-delivery](../architectures/luxleaf-delivery.md) | 0.2.0 | Artifact-bound release decisions | 4 |
| [luxleaf-containers](../architectures/luxleaf-containers.md) | 0.2.0 | Explicit argv container health checks | 4 |
| [luxleaf-model-lifecycle](../architectures/luxleaf-model-lifecycle.md) | 0.2.0 | Reviewed rollback to known active candidates | 4 |

## Reproducibility and validation

The private developer kit includes expanded_portfolio.py, which executes every repository’s expansion scenario. A scenario fails if a required result or rejection does not occur. Evidence records versions, exact commits and clean-checkout flags. The portfolio tests also deliberately bypass a document reader restriction and confirm the runner refuses to report success.

The source portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. All 31 installed wheels also passed their 174 component tests in a fresh environment. The [machine-readable expansion record](expansion-record.json) contains all 122 assertions and selected sanitized observations. Older five-journey and recovery records are preserved at their original commits and versions; their test totals are historical.

## Evidence boundaries

Identity, approval, resource capacity, latency samples and policy are synthetic host fixtures. Cloud and deployment components emit proposals only. SQLite operations and local text tools execute against disposable data. There are no live model-provider calls, cloud provisioning, notifications, paid operations or production measurements. Hashes bind content but are not signatures or proof of reviewer authenticity.

Public documentation CI checks coverage, links, clean-source flags and outcome structure. Private repository CI runs the package tests; cross-repository integration runs require the private local portfolio.
