# Read-only database inspection

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-data.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-data 0.2.0 · Infrastructure and delivery · October 31, 2026**

## Implemented contract

The Python helper luxleaf_data.core.inspect(database) opens an operator-selected SQLite file in read-only mode, checks integrity, and returns user_version and sorted application table names. It never creates a missing source and closes its connection after inspection.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Operator-selected SQLite file"]
    A["Operator-selected SQLite file"] --> B["Open read-only connection"]
    B["Open read-only connection"] --> C["Check integrity and schema version"]
    C["Check integrity and schema version"] --> D["Return table metadata"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `e4b906ff88e37328010549d0dea1e8ea050540a6`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Read-only inspection reports version and table | Passed |
| Inspection leaves database bytes unchanged | Passed |
| Missing database is rejected without creation | Passed |

```json
{
  "valid": true,
  "schema_version": 1,
  "tables": [
    "items"
  ]
}
```

The component test suite passed 7 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

The filesystem path is a trusted operator argument, not a remotely accepted payload. Schema inspection is not backup restoration or proof of application-level correctness. No row data is returned.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **deployment-recovery** through the recorded stages `restore`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
