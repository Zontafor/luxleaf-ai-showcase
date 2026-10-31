[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Retrieval evaluation

**luxleaf-evaluations · Governance and workflow · Component 0.1.0**

Measure retrieval results against a small set of explicitly labeled expectations.

## What works today

Precision, recall and reciprocal-rank evaluation against labeled cases.

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
    "k": 2,
    "cases": [
      {
        "id": "onboarding",
        "relevant": [
          "policy"
        ],
        "retrieved": [
          "policy",
          "other"
        ]
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "k": 2,
  "cases": [
    {
      "id": "onboarding",
      "precision_at_k": 0.5,
      "recall_at_k": 1.0,
      "reciprocal_rank": 1.0,
      "correct_abstention": null
    }
  ],
  "mean_reciprocal_rank": 1.0,
  "mean_recall_at_k": 1.0
}
```

## Behavior and boundaries

Each labeled case contains distinct relevant document identifiers and a ranked result list. Precision uses the requested k as denominator even when fewer results are returned. Recall is undefined for no-evidence cases; correct abstention is reported separately. Reciprocal rank is truncated at k.

These metrics evaluate retrieval ordering, not answer truthfulness or business value. Empty datasets and duplicate identifiers are rejected to avoid misleading aggregates. Use authorized representative labels before interpreting quality results.

## Where it connects

[model-governance](luxleaf-model-governance.md) · [model-lifecycle](luxleaf-model-lifecycle.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Representative business datasets and answer-faithfulness evaluation.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
