[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# API boundary

**luxleaf-api · Business knowledge · Component 0.1.0**

Derive tenant context from authenticated host credentials before calling a permitted operation.

## What works today

Tenant-bound authenticated in-process HTTP-style request dispatch.

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
    "op": "describe"
  }
}
```

**Recorded result**

```json
{
  "contract": "luxleaf-api/1",
  "request_fields": [
    "request_id",
    "payload"
  ],
  "tenant_source": "verified credential context",
  "transport": "in-process",
  "public_listener": false
}
```

## Behavior and boundaries

The Boundary class separates authentication, route lookup, role checks and handler invocation. It derives tenant identity from the host's credential registry and rejects tenant overrides in request bodies. Raw bearer tokens are hashed in the in-memory lookup. Error responses exclude request content and internal exception details.

This is an in-process HTTP-style dispatcher with no socket listener. Tokens are testable service credentials, not a full identity platform. Production transport, TLS, rate limits, expiration, rotation and external identity verification remain host responsibilities. The command-line example describes the contract without accepting credentials.

## Where it connects

[workspace](luxleaf-workspace.md) · [service-policy](luxleaf-service-policy.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 5 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Production HTTP hosting, OIDC and edge throttling.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
