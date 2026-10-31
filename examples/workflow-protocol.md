# Example: one workflow across clients

This is an illustrative interface contract for the private v0.3 foundation. It is not a public hosted API, runnable deployment, or application source release. Use synthetic questions during integration evaluation.

## Discover before selecting a model

An authenticated client obtains its tenant role's capabilities and model aliases. The catalog can indicate that a model is permitted but unavailable because remote execution is disabled. A catalog result does not bypass the next request's admission checks or guarantee provider availability.

## Submit the approved operation

The native workflow interface accepts JSON of this shape, with a tenant credential and a stable request identity supplied separately:

```json
{
  "workflow": "knowledge-query",
  "version": "1.0",
  "parameters": {
    "question": "What does the synthetic onboarding policy require?",
    "model": "local",
    "retrieve": true,
    "max_output_tokens": 512
  }
}
```

The response identifies a run. A separate worker processes the queue through the same model permissions, rate limits and budget accounting as interactive questions. Clients can list their tenant's runs, inspect status/output, or request cancellation.

## Exercise the meaningful cases

| Case | Expected behavior |
|---|---|
| Same submission identity and normalized parameters through JSON or legacy multipart | Resolve to the same run rather than queue duplicate work |
| Reused identity with a different question | Reject the conflicting request |
| Another tenant requests the run's output or cancellation | Deny access |
| Provider is disabled after the first accepted submission | Return the existing run on an otherwise matching submission replay |
| MCP workflow tools have not been enabled | Do not expose submission/cancellation tools |
| Remote workflow submission through MCP without remote permission | Reject the request |
| Worker encounters a revoked submitting credential | Do not execute the queued operation |
| Cancellation arrives after remote execution started | It may suppress workflow output but cannot guarantee stopping provider charges |

The Python client uses explicit request identities and does not automatically repeat paid operations after transport failures. An uncertain response calls for preserving the same identity and inspecting state, not creating a fresh attempt. Successful output can contain untrusted document text; the receiving application still needs appropriate display and tool-use controls.

See [integration status](../docs/INTEGRATIONS.md), [accounting and failure behavior](../docs/TECHNICAL_BRIEF.md#usage-and-cost-accounting), and [validation scope](../docs/VALIDATION.md).
