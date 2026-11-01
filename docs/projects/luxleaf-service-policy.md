[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Service authorization

**luxleaf-service-policy · Infrastructure and delivery · Component 0.2.0**

Make an explicit allow-or-deny decision for a service action and tenant.

## What works today

Deny-by-default service-to-service action authorization.

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
    "source": "workspace",
    "target": "knowledge",
    "action": "query",
    "rules": [
      {
        "source": "workspace",
        "target": "knowledge",
        "actions": [
          "query"
        ],
        "tenants": [
          "tenant-demo"
        ],
        "effect": "allow"
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "allowed": true,
  "reason": "explicit_allow"
}
```

## Behavior and boundaries

Service requests require an exact source, target, action and tenant match. Deny rules override allow rules, and absence of a matching allow denies access. Wildcards are not interpreted.

Policies are supplied by a trusted control plane. Source identifiers must come from verified workload identity; request strings alone do not authenticate a service. Decisions do not install network rules or establish TLS. Integrate with the API boundary and runtime before exposing service traffic.

## Connected demonstration

[Controlled agent work](../demonstrations/controlled-agent-work.md)

These journeys contain recorded executions that include this component.

## Where it connects

[api](luxleaf-api.md) · [cloud-tools](luxleaf-cloud-tools.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Workload identity verification and network enforcement.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Exact resource-scoped service rules** — A request may include a resource identifier and rules may contain resources. Scoped requests require an exact matching resource in a matching rule. Omitting the request resource cannot use a scoped rule; an unscoped rule cannot silently grant a scoped request. Explicit deny still takes precedence.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-service-policy.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
