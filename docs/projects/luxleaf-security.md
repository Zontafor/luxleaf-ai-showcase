[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Security posture

**luxleaf-security · Operational evidence · Component 0.2.0**

Identify missing deployment controls and show a concrete remediation for each.

## What works today

Deterministic deployment posture checks with actionable findings.

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
    "configuration": {
      "tls": true,
      "public_database": false,
      "workload_identity": true,
      "backups": true,
      "nonroot": true,
      "secret_logging": false,
      "dependency_scan": true
    }
  }
}
```

**Recorded result**

```json
{
  "passed": true,
  "findings": [],
  "controls_evaluated": 7,
  "certified": false
}
```

## Behavior and boundaries

Seven explicit deployment controls are evaluated. Missing values fail, and truthy strings or integers are not accepted as booleans. Findings include severity and a specific remediation without reflecting supplied configuration values.

The engine evaluates assertions, not infrastructure. A passing result does not prove the assertions are true, establish compliance or replace threat modeling, dependency inspection or penetration testing. Bind evidence collection to each control before using this as a release gate.

## Connected demonstration

[Evidence before release](../demonstrations/evidence-before-release.md)

These journeys contain recorded executions that include this component.

## Where it connects

[environments](luxleaf-environments.md) · [delivery](luxleaf-delivery.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Independent audit, threat testing and organization policy integration.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.

## Current package expansion

**Posture regression comparison** — Optional baseline_configuration is evaluated using the same controls as the current configuration. Comparison reports introduced, resolved and unchanged finding identifiers. A resolved finding never cancels an unrelated new failure.

[Inspect this component’s architecture, actual observations and rejection checks](../architectures/luxleaf-security.md). Version 0.2.0 passed 5 component tests locally. Earlier examples and validation notes on this page remain historical snapshots; the linked architecture page describes the current expansion.
