[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Model release governance

**luxleaf-model-governance · Governance and workflow · Component 0.1.0**

Decide whether a particular model artifact has the required independent approvals.

## What works today

Evaluate release evidence and separation-of-duty approvals.

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
    "author": "author",
    "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "checks": {
      "quality": true,
      "privacy": true,
      "security": true,
      "rollback": true
    },
    "approvals": [
      {
        "role": "security",
        "person": "reviewer-security",
        "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      },
      {
        "role": "release",
        "person": "reviewer-release",
        "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "approved": true,
  "failed_checks": [],
  "missing_roles": []
}
```

## Behavior and boundaries

A candidate's artifact hash binds its review. Four explicit boolean checks and independent security/release reviewers are required. The author cannot approve their own artifact, a person cannot fill both roles, and approvals cannot be transplanted to a different hash.

Identity and evidence authenticity must be established by the host. This engine evaluates structured records; it does not verify signatures, certify compliance or replace a release authority. Integrate approved decisions with the model registry's promotion gate.

## Connected demonstration

[Evidence before release](../demonstrations/evidence-before-release.md)

These journeys contain recorded executions that include this component.

## Where it connects

[evaluations](luxleaf-evaluations.md) · [model-lifecycle](luxleaf-model-lifecycle.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Signed evidence and organization-specific compliance processes.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
