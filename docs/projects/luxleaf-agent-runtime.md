[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Agent execution

**luxleaf-agent-runtime · Agents and tools · Component 0.2.0**

Execute a bounded sequence of registered local tools and retain its outcome.

## What works today

Execute approved local tool plans with step budgets and explicit failure records.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

The example starts with fresh, synthetic local state. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "steps": [
      {
        "id": "count",
        "tool": "text.count",
        "arguments": {
          "text": "Complete privacy training"
        }
      }
    ],
    "step_budget": 1
  }
}
```

**Recorded result**

```json
{
  "plan_sha256": "6b5706a81a2abbae58c09e77a1335bb9c895ec199b024361a6539d113cee9d2b",
  "status": "completed",
  "steps": [
    {
      "id": "count",
      "status": "completed",
      "result": {
        "words": 3
      }
    }
  ]
}
```

## Behavior and boundaries

The runtime owns its function registry and permits only two local read-only text operations. It validates the whole plan's names and identifiers before running the first step. Invalid arguments stop execution and produce a durable sanitized failure record. Request identity binds a canonical plan hash; a replay returns the stored execution record.

No remote or mutating tool can be enabled through payload fields. The database transaction is suitable for bounded local operations only. Adding external side effects requires durable checkpoints, approvals bound to plan hashes, and explicit uncertain-outcome handling before extending this registry.

## Connected demonstration

[Controlled agent work](../demonstrations/controlled-agent-work.md)

These journeys contain recorded executions that include this component.

## Where it connects

[agent-plans](luxleaf-agent-plans.md) · [events](luxleaf-events.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Durable execution checkpoints and process isolation.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Dependency-order enforcement** — Each step may supply depends_on. Dependencies must be unique and name already-listed steps; unresolved, cyclic or forward dependencies reject the entire plan before a tool runs. Valid ordered plans retain existing request fingerprint and replay behavior.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-agent-runtime.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
