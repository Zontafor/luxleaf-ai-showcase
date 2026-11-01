# Transitive rebuild planning

[All component architectures](../PORTFOLIO_ARCHITECTURE.md) · [Project page](../projects/luxleaf-developer-kit.md) · [All expansion evidence](../demonstrations/all-component-expansion.md)

**luxleaf-developer-kit 0.2.0 · Infrastructure and delivery · October 31, 2026**

## Implemented contract

The existing dependency graph accepts changed component names and returns rebuild_order containing those components and their transitive dependents in valid build order. Unknown changes fail; unrelated components are excluded.

## Component architecture

```mermaid
flowchart TD
    HOST[Trusted host identity and policy] --> A["Versioned component DAG"]
    A["Versioned component DAG"] --> B["Validate changed component set"]
    B["Validate changed component set"] --> C["Walk downstream dependencies"]
    C["Walk downstream dependencies"] --> D["Return minimal rebuild order"]
    B -. invalid input .-> REJECT[Bounded rejection or explicit denial]
```

This describes local responsibilities, not independently deployed cloud services. The host supplies verified identity and policy. An external model cannot grant itself actor, tenant or operator authority through these fields. Each component call owns its transaction; cross-component flows require explicit recovery.

## Recorded synthetic evidence

The new checked scenario ran against the private implementation at commit `764aa8bfc207cba4a45187e9147444e7357169ef`. Its source checkout was clean. Results below are selected actual observations; private credentials, local paths and implementation source are excluded.

| Executable check | Outcome |
|---|---|
| Upstream change rebuilds only transitive dependents | Passed |
| Leaf change avoids unrelated rebuilds | Passed |
| Invalid or unauthorized expansion request rejected | Passed |

```json
{
  "rebuild_order": [
    "base",
    "api",
    "ui"
  ]
}
```

The component test suite passed 5 tests locally. The full portfolio passed 174 component tests, 14 integration tests and 31 CLI examples. The all-component expansion record contains 122 assertions across 31 scenarios. Public CI verifies documentation and evidence structure; it does not execute private source.

## Operating boundary and future work

This computes a rebuild plan without invoking build tools or guaranteeing compatibility. Version strings are validated but dependency version ranges and lock resolution remain future work.

These checks use synthetic fixtures and local execution. They do not establish live-cloud acceptance, production scale, compliance certification or independent security assurance. Read the [portfolio architecture](../PORTFOLIO_ARCHITECTURE.md) for trust, state and deployment boundaries.

Original implementation remains proprietary to Michelle L. Wu in private repositories. Public materials follow the [showcase license](../../LICENSE).

## Subsequent integration release

Version 0.3.0 adds [persistent coordination and real process-interruption evidence](../demonstrations/coordinated-knowledge-recovery.md). This page preserves the earlier 0.2.0 expansion record; the new page describes the implemented cross-package flow and its current limits.
