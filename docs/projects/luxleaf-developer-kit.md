[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Developer tooling

**luxleaf-developer-kit · Infrastructure and delivery · Component 0.1.0**

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

## Where it connects

[delivery](luxleaf-delivery.md) · [containers](luxleaf-containers.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Package registry distribution and developer onboarding UI.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
