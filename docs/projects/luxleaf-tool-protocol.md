[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Tool protocol

**luxleaf-tool-protocol · Agents and tools · Component 0.1.0**

Expose a small, explicit local tool catalog with checked arguments.

## What works today

Versioned JSON tool discovery and permission-checked invocation.

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
    "method": "discover",
    "allowed_tools": [
      "text.count",
      "text.excerpt"
    ]
  }
}
```

**Recorded result**

```json
{
  "protocol": "luxleaf-tools/1",
  "tools": [
    {
      "name": "text.count",
      "description": "Count Unicode whitespace-separated words",
      "required": [
        "text"
      ],
      "effect": "read"
    },
    {
      "name": "text.excerpt",
      "description": "Return a bounded literal excerpt",
      "required": [
        "text",
        "limit"
      ],
      "effect": "read"
    }
  ]
}
```

## Behavior and boundaries

LuxLeaf tools/1 provides discovery and invocation for a deliberately small local registry. Tools have stable names, exact argument sets and declared effects. Unknown names, extra arguments and non-allowlisted calls are rejected.

The caller supplies a policy derived from trusted identity. This JSON contract is not MCP and does not advertise MCP compatibility. A future MCP adapter can translate protocol discovery and calls while retaining host approval and authorization behavior. No network listener or arbitrary code execution is included.

## Where it connects

[api](luxleaf-api.md) · [agent-runtime](luxleaf-agent-runtime.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: MCP transport/host interoperability via a dedicated adapter.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
