[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Inference engine

**luxleaf-inference · Business knowledge · Component 0.1.0**

Return inspectable source excerpts when a local answer is sufficient.

## What works today

Deterministic local extractive answers with tenant-bound evidence.

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
    "question": "What does onboarding require?",
    "citations": [
      {
        "tenant_id": "tenant-demo",
        "document_id": "policy",
        "text": "Complete privacy training before access."
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "mode": "local-excerpts",
  "answer": "Complete privacy training before access.",
  "citations": [
    {
      "document_id": "policy",
      "text": "Complete privacy training before access."
    }
  ],
  "abstained": false,
  "cost_micros": 0
}
```

## Behavior and boundaries

The original local engine returns bounded evidence excerpts and zero model cost. It abstains when no evidence is supplied. Every citation must match the trusted tenant context. It never transmits content or fabricates a model answer.

The caller provides authorized retrieved passages, typically from luxleaf-knowledge. A later provider adapter must define its own request contract, uncertainty handling, identity and usage accounting; it must not silently replace local execution.

## Where it connects

[rag](luxleaf-rag.md) · [metering](luxleaf-metering.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Live model-provider adapters and provider-specific accounting.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
