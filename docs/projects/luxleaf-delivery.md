[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Release delivery

**luxleaf-delivery · Infrastructure and delivery · Component 0.1.0**

Build a content-hash manifest and evaluate the required release-check assertions.

## What works today

Content-addressed release manifests and mandatory validation gates.

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
    "files": {
      "README.md": "Original LuxLeaf component"
    },
    "checks": {
      "unit_tests": true,
      "integration_tests": true,
      "secret_scan": true
    }
  }
}
```

**Recorded result**

```json
{
  "manifest": {
    "README.md": {
      "sha256": "8e17353132e36eea61a3a80f42c5ad6c9346eda5ad0dcc42c5b30a09812b882e",
      "bytes": 26
    }
  },
  "manifest_sha256": "08611c448c5a1fdbc6b997c8abdba34377a41cdfe66cc2270a1743c6b264abaf",
  "release_allowed": true,
  "failed_gates": [],
  "published": false
}
```

## Behavior and boundaries

Hash each supplied UTF-8 text file and a canonical manifest. Reject traversal, hidden paths and known private-key/database extensions. Required unit, integration and secret-scan assertions must all pass before release_allowed is true.

This module reads no arbitrary local paths and publishes nothing. It does not run the declared checks, discover all secrets, sign artifacts or attest to who produced evidence. Connect verified CI results and an artifact-signing authority before automated release. Binary packaging is outside this initial scope.

## Connected demonstration

[Evidence before release](../demonstrations/evidence-before-release.md)

These journeys contain recorded executions that include this component.

## Where it connects

[security](luxleaf-security.md) · [rollouts](luxleaf-rollouts.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Signed artifacts and remote build/deployment execution.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
