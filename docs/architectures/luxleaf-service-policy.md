# Exact resource-scoped service rules

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-service-policy.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-service-policy 0.2.0 · Infrastructure and delivery · October 31, 2026**

## Implemented contract

A request may include a resource identifier and rules may contain resources. Scoped requests require an exact matching resource in a matching rule. Omitting the request resource cannot use a scoped rule; an unscoped rule cannot silently grant a scoped request. Explicit deny still takes precedence.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Verified service context"]
    A["Verified service context"] --> B["Match tenant action and resource"]
    B["Match tenant action and resource"] --> C["Apply explicit deny precedence"]
    C["Apply explicit deny precedence"] --> D["Return authorization decision"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `e1478afed8886d6d75385a913eab50c421758d3b`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Exact allowed resource succeeds | Passed |
| Neighboring resource is denied | Passed |
| Omitting a resource cannot bypass a scoped rule | Passed |
| Explicit scoped deny overrides allow | Passed |

```json
{
  "allowed_resource": "document-a",
  "other_resource_allowed": false
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

Resources are bounded logical identifiers, not path globs. Service and tenant identities still need host verification; the evaluator does not enforce networks or issue credentials.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **agent-tools** through the recorded stages `agent-policy`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
