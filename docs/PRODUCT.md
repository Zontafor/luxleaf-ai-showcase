# Product overview

For capability status, actor responsibilities, and business evaluation, read the [Product & Technical Brief](TECHNICAL_BRIEF.md).

LuxLeaf AI is a development-stage platform for organizations that want to connect business knowledge to model access with consistent tenant permissions, usage controls, and workflow execution.

## An initial business workflow

An administrator adds an authorized text document to a tenant workspace. A team member asks a question. The platform retrieves relevant passages and either returns local excerpts or sends the question and passages to a configured model provider. A repeatable question can be submitted as a durable workflow. Administrators review recorded usage, uncertain outcomes, and execution state.

This workflow is implemented in the private development foundation. It is not a claim that LuxLeaf already supports every business domain, file format, or regulatory setting.

## Current boundaries

- Admin and member API keys define access within a tenant. Individual-user SSO, MFA, and invitation flows are not implemented.
- Documents are plain text or Markdown. Retrieval uses a bounded lexical index; it is not yet a vector-search product.
- Local answers are excerpts. Cloud-generated answers require a configured provider and may contain errors; citations identify retrieved evidence rather than proving answer correctness.
- Budget reservations and recorded token costs support operational control. They are not subscription billing, invoice reconciliation, or a guarantee of a maximum cloud bill.
- Workflows currently run an approved knowledge-query operation. They do not execute arbitrary uploaded code or general scientific workflow languages.
- Metadata-only tracing is opt-in. Document content and workflow results still exist in application storage and need appropriate retention and access controls.

## Product principles

**One set of controls.** Questions, tools, and workflows pass through the same gateway policies.

**Explicit data boundaries.** Local retrieval and remote model inference are distinguishable, and remote inference is disabled until configured.

**Evidence a person can inspect.** Source passages, recorded usage, and workflow states are visible to authorized users.

**Measured expansion.** New providers, workflow types, storage integrations, and deployment environments should follow concrete validation rather than a capability checklist.
