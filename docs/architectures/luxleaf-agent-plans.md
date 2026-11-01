# Dependency waves and plan identity

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-agent-plans.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-agent-plans 0.2.0 · Agents and tools · October 31, 2026**

## Implemented contract

Validated plans now include waves of steps whose dependencies are already satisfied, plus a SHA-256 digest of the normalized ordered plan. Independent roots share a wave. The digest covers tool, arguments, dependencies and declared effect.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Allowed tools and step DAG"]
    A["Allowed tools and step DAG"] --> B["Reject missing or cyclic dependencies"]
    B["Reject missing or cyclic dependencies"] --> C["Compute waves and plan digest"]
    C["Compute waves and plan digest"] --> D["Present plan for review"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `b83f9ad8875b4c5cb93d55cb5b41e816be1e2368`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Independent roots form one execution wave | Passed |
| Input order does not change approved plan identity | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "waves": [
    [
      "a",
      "b"
    ],
    [
      "c"
    ]
  ],
  "plan_sha256": "1e07a69dcb06401628d6e93c9817f85da819dbfa34da81bc1e7d262ea9f98e29"
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

Waves describe opportunities for concurrency; the planner does not execute them. The digest is not a signature. Effect classification and approvals must still be verified against a trusted tool registry.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Role in the full system

This component participates in **agent-tools** through the recorded stages `agent-plan`. These stages were executed in the 37-stage local acceptance composition. [Inspect the system pipeline handoffs and failure gates](../SYSTEM_PIPELINES.md), [deployment and state ownership](../SYSTEM_ARCHITECTURE.md), and [exact component commits and stage receipts](../demonstrations/system-pipeline-record.json). The linked record distinguishes local operations from unexecuted deployment proposals.
