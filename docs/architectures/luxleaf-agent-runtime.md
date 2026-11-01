# Dependency-order enforcement

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-agent-runtime.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-agent-runtime 0.2.0 · Agents and tools · October 31, 2026**

## Implemented contract

Each step may supply depends_on. Dependencies must be unique and name already-listed steps; unresolved, cyclic or forward dependencies reject the entire plan before a tool runs. Valid ordered plans retain existing request fingerprint and replay behavior.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Ordered local tool steps"]
    A["Ordered local tool steps"] --> B["Validate dependencies before execution"]
    B["Validate dependencies before execution"] --> C["Run registry with step budget"]
    C["Run registry with step budget"] --> D["Persist completed or failed result"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `5fb383556e793c0afe0cefe32b136589e2610583`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Invalid or unauthorized expansion request rejected | Passed |
| Valid ordered dependencies execute both steps | Passed |
| Rejected ordering did not poison the request identity | Passed |

```json
{
  "status": "completed",
  "executed_steps": 2
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

Execution remains local and sequential with fail-fast behavior. This does not add remote tools, isolation, durable step checkpoints or parallel execution.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).
