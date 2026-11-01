# Exact output budgets and passage deduplication

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-inference.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-inference 0.2.0 · Business knowledge · October 31, 2026**

## Implemented contract

The maximum character budget now includes separators between passages. Identical document/text pairs are emitted once, and omitted_passages counts duplicate or fully excluded passages. Every supplied citation is still checked for tenant identity, even after the budget is exhausted.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Tenant-checked evidence"]
    A["Tenant-checked evidence"] --> B["Remove duplicate passages"]
    B["Remove duplicate passages"] --> C["Apply total character budget"]
    C["Apply total character budget"] --> D["Return bounded cited excerpts"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `abfd194210a58299aeaec5f1a3dcd47c32c80bf4`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Total answer includes separator within five-character limit | Passed |
| Repeated identical passage is omitted | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "answer_characters": 5,
  "omitted_passages": 1
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

The budget counts Python characters, not model tokens or bytes. Partially included passages are truncated excerpts, not generated summaries. There is no provider call.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **access-knowledge** through the recorded stages `infer`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
