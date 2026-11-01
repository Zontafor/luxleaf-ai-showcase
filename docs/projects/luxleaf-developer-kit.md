[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Developer tooling

**luxleaf-developer-kit · Infrastructure and delivery · Component 0.3.0**

Determine a reproducible build order for a closed component dependency graph.

## What works today

Validate component dependency manifests and compute build order.

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
    "components": [
      {
        "name": "luxleaf-knowledge",
        "version": "0.1.0"
      },
      {
        "name": "luxleaf-rag",
        "version": "0.1.0",
        "dependencies": [
          "luxleaf-knowledge"
        ]
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "build_order": [
    "luxleaf-knowledge",
    "luxleaf-rag"
  ],
  "components": 2,
  "external_dependencies": []
}
```

## Behavior and boundaries

Validate a closed component manifest and calculate a stable dependency-first build order. Duplicate components, unknown dependencies, malformed version numbers and cycles are rejected.

This verifies graph shape, not dependency version compatibility or package authenticity. Dependencies here represent integration/build relationships; components otherwise run independently. Private registry publication and signed package resolution are separate future capabilities.

## Connected demonstration

[Evidence before release](../demonstrations/evidence-before-release.md)

These journeys contain recorded executions that include this component.

## Where it connects

[delivery](luxleaf-delivery.md) · [containers](luxleaf-containers.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Package registry distribution and developer onboarding UI.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Recovery runner expansion

Version 0.1.1 adds a reproducible [event/archive recovery exercise](../demonstrations/event-delivery-recovery.md) with ten assertions and sanitized output. This extends the five-journey portfolio runner. The public pages show recorded results; the runner source remains private.

## Current package expansion

**Transitive rebuild planning** — The existing dependency graph accepts changed component names and returns rebuild_order containing those components and their transitive dependents in valid build order. Unknown changes fail; unrelated components are excluded.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-developer-kit.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.

## Version 0.3.0: durable integration

The [coordinated knowledge recovery demonstration](../demonstrations/coordinated-knowledge-recovery.md) exercises a persistent six-stage workflow using real worker-process exits. The workflow package provides the coordinator and knowledge composition; developer kit provides the reproducible fault runner and cross-package suite. Earlier expansion examples remain historical snapshots.
