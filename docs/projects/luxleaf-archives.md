[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Evidence archives

**luxleaf-archives · Operational evidence · Component 0.1.0**

Keep a local chain of event records whose contents can be checked against a retained digest.

## What works today

Local tenant event archive with chained hashes and tamper verification.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

One synthetic event was appended to the local archive before verifying its sequence and digest. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "verify"
  }
}
```

**Recorded result**

```json
{
  "valid": true,
  "entries": 1,
  "head_sha256": "b606b230b7d44d352a5f26eddb0bf8b5dc2076b3b289f65cbd0efbd210884486"
}
```

## Behavior and boundaries

Archive entries form a SHA-256 chain over canonical JSON, sequence and previous digest. Every append verifies the existing chain. Stable event identifiers permit exact replay and reject conflicting content. Tenant identity is checked before storing events.

This detects accidental corruption or changes relative to a trusted head digest. A database administrator can rewrite the entire chain; without a separately retained signed head this is not tamper-proof storage. No encryption, Object Lock, external signing, retention deletion or remote delivery is provided.

## Where it connects

[events](luxleaf-events.md) · [incidents](luxleaf-incidents.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Remote retention, signing and immutable storage.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
