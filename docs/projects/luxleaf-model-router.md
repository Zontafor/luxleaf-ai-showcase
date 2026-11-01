[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Model routing

**luxleaf-model-router · Governance and workflow · Component 0.2.0**

Choose an eligible model proposal within a tenant’s region and budget policy.

## What works today

Deterministic selection by permissions, region, capacity and estimated cost.

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
    "allowed_models": [
      "local"
    ],
    "region": "local",
    "budget_micros": 0,
    "models": [
      {
        "id": "local",
        "remote": false,
        "regions": [
          "local"
        ],
        "estimated_cost_micros": 0,
        "latency_ms": 1,
        "remaining_capacity": 10
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "selected": "local",
  "rejected": [],
  "reservation_required": true
}
```

## Behavior and boundaries

Filter candidates by tenant permission, remote-execution consent, region, capacity and estimated cost. Select deterministically by cost, latency and model identifier. No provider is probed or invoked.

A result is a proposal, not a reservation. The integrating gateway must atomically reserve budget and capacity and recheck current policy immediately before execution. Caller-supplied health and pricing can be stale; this module alone does not guarantee availability or cost ceilings.

## Connected demonstration

[Knowledge with permission](../demonstrations/knowledge-with-permission.md)

These journeys contain recorded executions that include this component.

## Where it connects

[metering](luxleaf-metering.md) · [inference](luxleaf-inference.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Live provider health and latency telemetry.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Latency-aware routing and fallback order** — Strategy accepts cost or latency, with cost remaining the default. Optional max_latency_ms excludes candidates beyond the supplied threshold. Eligible candidates are returned in stable preference order after permissions, region, remote policy, capacity and budget checks.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-model-router.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
