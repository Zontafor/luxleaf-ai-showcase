[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Workflow queue

**luxleaf-workflows · Governance and workflow · Component 0.3.0**

Keep approved work durable while distinguishing queued, running and uncertain execution.

## What works today

Durable tenant jobs with leases, fencing and cancellation.

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
    "op": "submit",
    "key": "onboarding-1",
    "input": {
      "question": "What does onboarding require?"
    }
  }
}
```

**Recorded result**

```json
{
  "id": "onboarding-1",
  "input": {
    "question": "What does onboarding require?"
  },
  "fingerprint": "81362cd27fbff22d721c09cf8577ed1b1f27a8e87e2ccbef3b80539cb5d17cdf",
  "status": "queued",
  "fence": 0,
  "attempts": 0
}
```

## Behavior and boundaries

Submission keys and canonical input hashes prevent conflicting reuse. Claims produce a lease token and monotonically advancing fence. Completion requires a live matching lease. Expiration transitions work to uncertain; it does not automatically run possibly billable work twice.

Queued cancellation is terminal. Cancellation after execution starts marks uncertainty because external effects cannot be recalled. No arbitrary code is run by this queue. An integrating worker selects an approved handler and separately reconciles external effects. This v1 implementation intentionally omits automatic uncertain-job recovery and heartbeats.

## Connected demonstration

[Knowledge with permission](../demonstrations/knowledge-with-permission.md)

These journeys contain recorded executions that include this component.

## Where it connects

[rag](luxleaf-rag.md) · [events](luxleaf-events.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 5 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Isolated remote execution and distributed load validation.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Active workflow lease renewal** — Renew requires job id, matching lease_token and fence, and optional lease_seconds from 1 to 3600. It extends expiry to the greater of existing expiry or current host time plus duration. The fence and worker claim remain unchanged. Expired, uncertain or completed work cannot renew.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-workflows.md). Version 0.2.0 passed 6 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.

## Version 0.3.0: durable integration

The [coordinated knowledge recovery demonstration](../demonstrations/coordinated-knowledge-recovery.md) exercises a persistent six-stage workflow using real worker-process exits. The workflow package provides the coordinator and knowledge composition; developer kit provides the reproducible fault runner and cross-package suite. Earlier expansion examples remain historical snapshots.
