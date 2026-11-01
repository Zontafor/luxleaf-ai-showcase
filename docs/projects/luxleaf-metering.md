[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Usage metering

**luxleaf-metering · Governance and workflow · Component 0.2.0**

Reserve estimated usage before a request and keep uncertain spending visible.

## What works today

Durable credit reservations, replay checks and settlement.

This page is publicly readable without source-repository access. It contains a recorded local demonstration and product documentation. The implementation is private; no hosted application endpoint is advertised here.

## See an actual example

The local demonstration tenant was assigned 100 credit units measured in millionths before reserving 20 for a synthetic request. These are test values, not a product price. The following request and result were captured by running the private component on synthetic data for this public page. No cloud service was called.

**Request**

```json
{
  "schema_version": 1,
  "tenant_id": "tenant-demo",
  "request_id": "example-1",
  "payload": {
    "op": "reserve",
    "key": "question-1",
    "reserve_micros": 20,
    "operation": {
      "question": "Synthetic onboarding question"
    }
  }
}
```

**Recorded result**

```json
{
  "entry": {
    "fingerprint": "03b54a94d690852b461d0f1c8ef640734d8cc619dbf693ddb42ea02de62d7f19",
    "reserved": 20,
    "status": "reserved"
  },
  "replayed": false
}
```

## Behavior and boundaries

Credit is represented by integer millionths of a currency unit. Reservations serialize in the local database and compare stable operation fingerprints on replay. Unknown outcomes keep their hold. Settlement is idempotent only for the same actual amount.

Verified actual usage may exceed its estimate: settlement records the real cost and reports an over-limit balance instead of concealing the overage. Further reservations are denied. Configure and settle are trusted operator operations; this engine is not an invoice system or a hard provider-spend ceiling. Currency and pricing policy belong to the integrating service.

## Connected demonstration

[Knowledge with permission](../demonstrations/knowledge-with-permission.md)

These journeys contain recorded executions that include this component.

## Where it connects

[model-router](luxleaf-model-router.md) · [workflows](luxleaf-workflows.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Provider invoice reconciliation and commercial billing.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Reviewed unknown-usage reconciliation** — Reconcile accepts key, actual_micros, actor and evidence_ref only when the reservation is unknown. It records the review and settles exact usage, releasing unused held credit. Invalid reviews roll back without changing the hold.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-metering.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
