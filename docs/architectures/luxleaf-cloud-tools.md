# Region constraints and unambiguous resource paths

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-cloud-tools.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-cloud-tools 0.2.0 · Agents and tools · October 31, 2026**

## Implemented contract

A policy containing regions requires a matching request region. Resource paths and policy prefixes reject dot segments, backslashes and percent encoding; wildcard restrictions remain. This prevents obvious alternative path representations from bypassing prefix intent.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Account and resource proposal"]
    A["Account and resource proposal"] --> B["Reject ambiguous path encodings"]
    B["Reject ambiguous path encodings"] --> C["Apply region and prefix policy"]
    C["Apply region and prefix policy"] --> D["Return unexecuted inventory plan"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `0215912105eea43ff7effd857ff7a43e22caba1e`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Region-scoped plan is accepted without execution | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "region": "local",
  "executed": false,
  "ambiguous_paths_rejected": 3
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

The model is a narrow inventory proposal policy, not a universal parser for provider resource names. It does not contact providers, verify account identity or execute actions.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **agent-tools** through the recorded stages `cloud-policy`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
