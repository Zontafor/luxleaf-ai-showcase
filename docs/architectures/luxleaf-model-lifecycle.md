# Reviewed rollback to known active candidates

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-model-lifecycle.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-model-lifecycle 0.2.0 · Governance and workflow · October 31, 2026**

## Implemented contract

Rollback requires a previously promoted target, matching current expected_active, artifact-matching approval, quality threshold, actor and evidence_ref. It switches the local active pointer and records rollback history. A registered but never-active candidate cannot be a rollback target.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Current model and reviewed target"]
    A["Current model and reviewed target"] --> B["Check expected active and prior promotion"]
    B["Check expected active and prior promotion"] --> C["Validate artifact approval and quality"]
    C["Validate artifact approval and quality"] --> D["Record local registry rollback"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `8be3fd1056959976cf5f3b862b570c60345ee2e2`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Invalid or unauthorized expansion request rejected | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Reviewed rollback restores a previously active candidate | Passed |
| Rollback leaves evidence in registry history | Passed |

```json
{
  "active": "one",
  "rolled_back": true
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

This changes registry state only, not deployed model traffic or files. Approval fields are trusted host assertions. Rollback is manual and reviewed, not automatic drift response.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **governed-release** through the recorded stages `candidate`, `promote`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
