[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Release rollouts

**luxleaf-rollouts · Infrastructure and delivery · Component 0.1.0**

Use observation thresholds to propose holding, promoting or rolling back a candidate.

## What works today

Canary promotion/rollback decisions using explicit observation gates.

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
    "op": "start",
    "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

**Recorded result**

```json
{
  "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "status": "canary",
  "traffic_percent": 10,
  "observations": 0
}
```

## Behavior and boundaries

A rollout begins with a digest-pinned candidate and limited traffic percentage. Insufficient samples hold the rollout. A breached error-rate or p95 latency threshold requests rollback; passing observations increase the proposed percentage until promotion.

Thresholds and observations come from a trusted release controller. The decision engine does not switch traffic or prove that observations describe the candidate image. Persist and bind external observation evidence before using decisions for automatic deployment.

## Connected demonstration

[Deployment planning and recovery](../demonstrations/deployment-planning-and-recovery.md)

These journeys contain recorded executions that include this component.

## Where it connects

[observability](luxleaf-observability.md) · [delivery](luxleaf-delivery.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Actual traffic switching and deployment control.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
