[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Workspace membership

**luxleaf-workspace · Business knowledge · Component 0.2.0**

Decide whether a workspace member may read, edit or manage business information.

## What works today

Persistent tenant memberships and role-based access decisions.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

A synthetic workspace was initialized with an owner and a reader. The request asks whether that reader may write. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "authorize",
    "actor": "reader",
    "action": "write"
  }
}
```

**Recorded result**

```json
{
  "allowed": false
}
```

## Behavior and boundaries

A workspace contains active members with admin, editor or reader roles. Bootstrap is allowed once per tenant. Administrators manage memberships; the last active administrator cannot remove their own authority. Every mutation is transactional.

This is a local membership engine, not a login system. The host must derive tenant and actor from verified identity; supplied actor identifiers are not credentials. Integrate authorization decisions with luxleaf-api before exposing application operations. SSO, invitations and audit export are further work.

## Connected demonstration

[Knowledge with permission](../demonstrations/knowledge-with-permission.md)

These journeys contain recorded executions that include this component.

## Where it connects

[api](luxleaf-api.md) · [service-policy](luxleaf-service-policy.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Identity-provider login and a dedicated user interface.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Membership revisions and audit** — For member updates, optional expected_revision must equal the current revision. Each accepted member update advances the revision and records actor, target, previous membership and current membership. Administrators can request op=audit. Bootstrap remains revision zero.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-workspace.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
