[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Batch scheduling

**luxleaf-batch · Infrastructure and delivery · Component 0.1.0**

Fit proposed jobs into a supplied CPU and memory capacity snapshot.

## What works today

Deterministic CPU/memory-constrained job placement with deferred-job reporting.

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
    "nodes": [
      {
        "id": "worker-1",
        "cpu": 4,
        "memory_mib": 8192
      }
    ],
    "jobs": [
      {
        "id": "onboarding",
        "tenant_id": "tenant-demo",
        "cpu": 1,
        "memory_mib": 512
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "placements": [
    {
      "job_id": "onboarding",
      "node_id": "worker-1"
    }
  ],
  "deferred": [],
  "remaining": [
    {
      "id": "worker-1",
      "cpu": 3,
      "memory_mib": 7680
    }
  ],
  "executed": false
}
```

## Behavior and boundaries

Jobs are sorted by priority, memory, CPU and identifier. Each is placed on the tightest fitting node using memory then CPU as tie breakers. Capacity is decremented immediately in the proposed plan; unschedulable jobs are explicitly deferred. Tenant identities must match the caller context.

This is a deterministic placement calculation over a supplied capacity snapshot, not a cluster scheduler or compute executor. A real executor needs atomic resource reservations, isolated containers, cancellation and reconciliation of actual worker capacity.

## Connected demonstration

[Deployment planning and recovery](../demonstrations/deployment-planning-and-recovery.md)

These journeys contain recorded executions that include this component.

## Where it connects

[workflows](luxleaf-workflows.md) · [runtime](luxleaf-runtime.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Actual isolated compute execution and cluster scheduling.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
