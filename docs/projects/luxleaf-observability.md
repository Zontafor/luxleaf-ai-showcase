[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Service objectives

**luxleaf-observability · Operational evidence · Component 0.1.0**

Calculate request-window availability, latency percentiles and budget consumption.

## What works today

Latency percentiles, availability and error-budget calculations.

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
    "target_basis_points": 9900,
    "samples": [
      {
        "latency_ms": 12,
        "status_code": 200
      },
      {
        "latency_ms": 20,
        "status_code": 200
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "observed_requests": 2,
  "server_errors": 0,
  "availability": 1.0,
  "p50_ms": 12,
  "p95_ms": 20,
  "budget_consumed": 0.0,
  "status": "within_budget"
}
```

## Behavior and boundaries

Availability counts responses below HTTP 500 as successful under this explicit policy. Latency uses nearest-rank percentiles. Error-budget consumption compares observed server errors to the allowance implied by the target and observed request count. Empty windows report no_data rather than perfect availability.

The caller defines and collects a representative window; the module has no live metric backend. Client errors, timeouts without responses, tenant fairness and end-to-end availability may require a different SLI definition. No alert is sent.

## Connected demonstration

[Operational evidence and response](../demonstrations/operational-evidence-and-response.md)

These journeys contain recorded executions that include this component.

## Where it connects

[telemetry](luxleaf-telemetry.md) · [rollouts](luxleaf-rollouts.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Live metric ingestion and alert delivery.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
