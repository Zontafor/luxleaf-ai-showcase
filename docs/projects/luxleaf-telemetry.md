[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Telemetry privacy

**luxleaf-telemetry · Operational evidence · Component 0.1.0**

Prepare bounded operational metadata while dropping unapproved content fields.

## What works today

Allowlisted bounded operational spans with tenant pseudonyms.

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
    "operation": "retrieval",
    "status": "ok",
    "duration_ms": 12,
    "attributes": {
      "citations": 2,
      "question": "THIS FIELD IS DROPPED"
    }
  }
}
```

**Recorded result**

```json
{
  "span": {
    "tenant_pseudonym": "a1c5b1ff48ff5e7151ee75a043605e6f287b7943a34050c3a9863253558d7301",
    "operation": "retrieval",
    "status": "ok",
    "duration_ms": 12,
    "attributes": {
      "citations": 2
    }
  },
  "dropped_attribute_count": 1,
  "exported": false
}
```

## Behavior and boundaries

Produce bounded operational spans with an allowlist of numeric attributes. Question text, arbitrary labels and exception strings are dropped. Operation and status values are enumerated. Tenant identifiers are replaced with HMAC pseudonyms using a random per-tenant key retained in local state.

Without persistent state, pseudonyms change between calls. Protect the state database, and define key rotation and retention before deployment. Pseudonyms are not proof of anonymization. Only the span object is intended for export; the surrounding local request envelope still contains the caller's tenant and request identifiers. No collector transport is included.

## Where it connects

[observability](luxleaf-observability.md) · [incidents](luxleaf-incidents.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Collector transport, key management and retention.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
