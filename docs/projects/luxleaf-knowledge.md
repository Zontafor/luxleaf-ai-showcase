[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Knowledge retrieval

**luxleaf-knowledge · Business knowledge · Component 0.2.0**

Find an authorized policy passage that answers a team member’s question.

## What works today

Persistent tenant documents, bounded passage retrieval and citations.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

One synthetic policy was stored in tenant-demo before this retrieval request. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "query",
    "question": "What privacy training is required?",
    "limit": 3
  }
}
```

**Recorded result**

```json
{
  "citations": [
    {
      "tenant_id": "tenant-demo",
      "document_id": "onboarding-policy",
      "title": "Synthetic onboarding policy",
      "offset": 0,
      "text": "Complete privacy training before receiving workspace access.",
      "score": 0.4
    }
  ],
  "found": true
}
```

## Behavior and boundaries

Documents are stored per tenant. Text is split into deterministic 1,000-character passages. Ranking is the fraction of distinct question terms found in each passage, with stable document/offset tie breaking. Only passages with positive overlap are returned.

The database transaction covers document updates and queries. At most 100 documents, 100,000 characters each and 20 citations per query are accepted; the shared state byte limit may be reached first. This is lexical evidence retrieval, not semantic search. Passages remain untrusted content. Deletion affects subsequent retrieval, not copies retained by callers.

## Connected demonstration

[Knowledge with permission](../demonstrations/knowledge-with-permission.md)

These journeys contain recorded executions that include this component.

## Where it connects

[rag](luxleaf-rag.md) · [evaluations](luxleaf-evaluations.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Embedding search, document ACLs and binary document ingestion.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Document reader restrictions** — Put accepts readers as a bounded list of actor identifiers. Omission on a new document means tenant-wide visibility; omission on update preserves its current readers. An empty list denies all query/list readers. Query and list filter restricted records using the host-derived actor before returning passages or titles.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-knowledge.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
