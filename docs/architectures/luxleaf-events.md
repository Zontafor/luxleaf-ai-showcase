# Managed event lease renewal

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-events.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-events 0.3.0 · Operational evidence · October 31, 2026**

## Implemented contract

Renew requires the same consumer, event hash, worker, fence and active credential as completion. A bounded lease_seconds extends expiry without advancing attempts or changing the fence. Renewal preserves the active token hash; uncertain, expired and terminal deliveries cannot renew.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Claimed consumer delivery"]
    A["Claimed consumer delivery"] --> B["Validate current lease and fence"]
    B["Validate current lease and fence"] --> C["Extend active expiry"]
    C["Extend active expiry"] --> D["Complete or reconcile outcome"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `cc77bb668023eef79c1d641550e4e6d113f481e2`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Invalid or unauthorized expansion request rejected | Passed |
| Renewal preserves fence | Passed |
| Renewal extends the active claim | Passed |
| Renewal does not release the event | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "renewed": true,
  "fence": 1,
  "completed": true
}
```

The component test suite passed 19 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

This extends Events 0.2 recovery semantics. Repeated valid renewals can extend ownership; the host should enforce a workload deadline. Expiry remains lazily observed, and no remote sink fencing is implied.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **operations-response** through the recorded stages `event`, `pending`, `acknowledge`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
