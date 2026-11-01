[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Cloud action policy

**luxleaf-cloud-tools · Agents and tools · Component 0.2.0**

Decide whether an inventory action fits an account and resource policy.

## What works today

Evaluate narrowly scoped inventory actions against account/resource policy.

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
    "account": "000000000000",
    "service": "storage",
    "action": "inventory.list",
    "resource": "tenant-demo/documents/",
    "policy": {
      "accounts": [
        "000000000000"
      ],
      "actions": [
        "inventory.list"
      ],
      "resource_prefixes": {
        "storage": [
          "tenant-demo/"
        ]
      }
    }
  }
}
```

**Recorded result**

```json
{
  "account": "000000000000",
  "service": "storage",
  "action": "inventory.list",
  "resource": "tenant-demo/documents/",
  "authorized_plan": true,
  "executed": false
}
```

## Behavior and boundaries

An operator-supplied policy bounds account identifiers, read-only inventory actions and resource prefixes. Prefixes must end at a slash boundary. Wildcard requests and unsupported actions are denied. The result is an execution plan only.

This module holds no cloud credentials, uses no provider SDK and performs no remote action. An eventual executor must revalidate the plan against verified workload identity and provider-specific resource naming; the generic names here are not IAM resource identifiers.

## Connected demonstration

[Controlled agent work](../demonstrations/controlled-agent-work.md)

These journeys contain recorded executions that include this component.

## Where it connects

[service-policy](luxleaf-service-policy.md) · [agent-plans](luxleaf-agent-plans.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Authenticated provider-specific execution adapters.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Region constraints and unambiguous resource paths** — A policy containing regions requires a matching request region. Resource paths and policy prefixes reject dot segments, backslashes and percent encoding; wildcard restrictions remain. This prevents obvious alternative path representations from bypassing prefix intent.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-cloud-tools.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
