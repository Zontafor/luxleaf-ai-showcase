[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Event outbox

**luxleaf-events · Operational evidence · Component 0.2.0**

Retain operational events until each consumer acknowledges its own delivery.

## What works today

Durable deduplicated tenant events with consumer-specific acknowledgements, exclusive delivery claims, bounded retries and explicit recovery.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

A synthetic workflow-completion event was appended before this consumer requested pending events. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "pending",
    "consumer": "archive"
  }
}
```

**Recorded result**

```json
{
  "events": [
    {
      "id": "event-1",
      "kind": "workflow.completed",
      "payload": {
        "workflow_id": "onboarding-1"
      },
      "sha256": "e0170dc96e3b7ee63bfa3b8571a9f503fcf79887b44319e0663ebb64f220242f",
      "tenant_id": "tenant-demo"
    }
  ]
}
```

## Behavior and boundaries

Append assigns stable content hashes to tenant-scoped event identifiers. Reusing an identifier with different content fails. Each consumer has independent acknowledgements, bound to the event hash; delivery success must precede acknowledgement.

Version 0.2 adds managed claims with active credentials and fences. Expired leases become uncertain and require operator reconciliation. Known retryable failures use bounded delays and an attempt budget. Pending reads remain a legacy inspection view; managed workers use claim. Once claimed, legacy acknowledgements cannot bypass lease checks. The [recovery architecture and exercise](../demonstrations/event-delivery-recovery.md) explains the protocol and upgrade boundaries.

## Connected demonstration

[Operational evidence and response](../demonstrations/operational-evidence-and-response.md)

These journeys contain recorded executions that include this component.

## Where it connects

[archives](luxleaf-archives.md) · [observability](luxleaf-observability.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 18 component tests passed locally for version 0.2.0.
- The expanded portfolio passed 143 component tests, 12 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Remote delivery, lease renewal, retention and measured capacity.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
