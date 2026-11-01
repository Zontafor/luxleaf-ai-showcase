# Explicit argv container health checks

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-containers.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-containers 0.2.0 · Infrastructure and delivery · October 31, 2026**

## Implemented contract

Optional health_command is a nonempty bounded argv array. Generated Compose uses CMD exec form, with bounded interval, timeout and retries. Explicit CMD/CMD-SHELL markers are rejected as executable names; existing nonroot, read-only and capability restrictions remain.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Digest-pinned container request"]
    A["Digest-pinned container request"] --> B["Validate bounded health argv"]
    B["Validate bounded health argv"] --> C["Preserve restricted service settings"]
    C["Preserve restricted service settings"] --> D["Return unstarted Compose definition"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `a350e45e6d8a0579601c91f40aa3e1064be48041`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Health command uses explicit argv rather than implicit shell | Passed |
| Health checks preserve read-only runtime | Passed |
| Invalid or unauthorized expansion request rejected | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "healthcheck": {
    "test": [
      "CMD",
      "python",
      "-V"
    ],
    "interval": "30s",
    "timeout": "5s",
    "retries": 3
  },
  "started": false
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

The command is trusted host configuration and may itself name an interpreter; this is not a command sandbox. The image must contain the chosen executable. No container is started or image pulled.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **deployment-recovery** through the recorded stages `container`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
