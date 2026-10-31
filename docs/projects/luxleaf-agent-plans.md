[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Agent planning

**luxleaf-agent-plans · Agents and tools · Component 0.1.0**

Review tool steps and dependencies before an execution runtime receives them.

## What works today

Validate and order bounded tool plans with explicit approval requirements.

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
    "allowed_tools": [
      "text.count"
    ],
    "steps": [
      {
        "id": "count",
        "tool": "text.count",
        "arguments": {
          "text": "Synthetic onboarding policy"
        }
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "steps": [
    {
      "id": "count",
      "tool": "text.count",
      "depends_on": [],
      "effect": "read",
      "arguments": {
        "text": "Synthetic onboarding policy"
      }
    }
  ],
  "approval_required": [],
  "executed": false
}
```

## Behavior and boundaries

Plans contain at most 50 uniquely identified steps. Every tool must be allowlisted; dependency identifiers must exist; cycles are rejected. A stable topological ordering makes review reproducible. Write and remote steps are separately listed as requiring approval.

Effect classifications must come from a trusted tool registry when integrated, not from an untrusted model's declaration. This planner does not authorize or execute tools. The runtime must enforce tool policy again and bind any approval to the exact reviewed plan.

## Connected demonstration

[Controlled agent work](../demonstrations/controlled-agent-work.md)

These journeys contain recorded executions that include this component.

## Where it connects

[agent-runtime](luxleaf-agent-runtime.md) · [tool-protocol](luxleaf-tool-protocol.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: An interactive plan review experience.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
