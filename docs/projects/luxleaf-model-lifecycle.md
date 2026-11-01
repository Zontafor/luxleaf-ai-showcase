[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Model registry

**luxleaf-model-lifecycle · Governance and workflow · Component 0.2.0**

Maintain a candidate registry and promote an approved artifact that meets a quality gate.

## What works today

Durable candidate registration and evidence-gated model promotion.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

A synthetic candidate with a quality score of 9,500 basis points was registered. The example supplies a synthetic matching approval; real approval evidence must come from a trusted authority. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "promote",
    "id": "candidate-1",
    "approval": {
      "approved": true,
      "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    "minimum_quality_basis_points": 9000
  }
}
```

**Recorded result**

```json
{
  "active": "candidate-1",
  "artifact_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "promotions": 1
}
```

## Behavior and boundaries

Candidates bind a stable identifier, artifact digest and evaluated quality score. Promotion requires the exact artifact's approved governance decision and a configured quality threshold. The active pointer and promotion history change atomically. Repeating promotion of the current candidate does not duplicate history.

Governance decisions and evaluation scores must be supplied by trusted services. This local registry does not train models, store binaries, verify signatures, collect drift data or perform live deployment. Keep actual artifacts in access-controlled storage and bind their checksum to this registry.

## Connected demonstration

[Evidence before release](../demonstrations/evidence-before-release.md)

These journeys contain recorded executions that include this component.

## Where it connects

[model-governance](luxleaf-model-governance.md) · [evaluations](luxleaf-evaluations.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: External model artifact storage, drift monitoring and rollback automation.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Reviewed rollback to known active candidates** — Rollback requires a previously promoted target, matching current expected_active, artifact-matching approval, quality threshold, actor and evidence_ref. It switches the local active pointer and records rollback history. A registered but never-active candidate cannot be a rollback target.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-model-lifecycle.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
