# Idempotent rollout observations

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-rollouts.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-rollouts 0.2.0 · Infrastructure and delivery · October 31, 2026**

## Implemented contract

Optional observation_id binds all observation input fields to its recorded decision within the active rollout. Exact replay returns the earlier decision without advancing traffic again. Reusing the identifier with changed metrics or policy fails. Starting a new rollout clears its observation history.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Canary observation window"]
    A["Canary observation window"] --> B["Check identity and content fingerprint"]
    B["Check identity and content fingerprint"] --> C["Evaluate evidence once"]
    C["Evaluate evidence once"] --> D["Persist rollout decision"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `1c3293ba2c030bf7a3c17141a285b956e721daaa`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| First observation advances canary | Passed |
| Exact observation replay cannot advance twice | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Conflict leaves traffic proposal unchanged | Passed |

```json
{
  "traffic_percent": 35,
  "duplicate_observation_advanced": false
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

Legacy observations without identifiers remain non-idempotent. Hosts must use unique observation identities per rollout and associate metrics with the correct release. Returned percentages are proposals, not traffic changes.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **deployment-recovery, operations-response** through the recorded stages `rollout`, `rollback`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
