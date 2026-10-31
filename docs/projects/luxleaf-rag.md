[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Knowledge orchestration

**luxleaf-rag · Business knowledge · Component 0.1.0**

Connect retrieval and inference while checking tenant identity and evidence excerpts.

## What works today

Compose tenant-filtered retrieval and local inference with verifiable citations.

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
    "question": "What is required?",
    "citations": [
      {
        "tenant_id": "tenant-demo",
        "document_id": "policy",
        "text": "Complete privacy training."
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "answer": "Complete privacy training.",
  "citations": [
    {
      "document_id": "policy",
      "text": "Complete privacy training."
    }
  ],
  "abstained": false,
  "question_sha256": "0bdf754eca51a84cecd7d1b83f0e442451e59a3819d6dde70093dbc2f88313bc"
}
```

## Behavior and boundaries

The Python pipeline accepts retrieval and inference callbacks. It checks tenant identity on retrieved passages and verifies that returned citation excerpts actually occur in those passages. A nonempty answer requires evidence. The standalone JSON example uses local excerpts.

A citation-substring check is not a semantic faithfulness proof: a generated answer may still contradict its citations. Callback implementations are trusted code, not supplied source strings. Integration tests connect this pipeline to the independent knowledge and inference repositories.

## Where it connects

[knowledge](luxleaf-knowledge.md) · [inference](luxleaf-inference.md) · [workflows](luxleaf-workflows.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Live gateway integration and representative quality measurement.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
