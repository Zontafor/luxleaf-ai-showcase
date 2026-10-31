# Explore LuxLeaf projects

**31 public project pages · Original LuxLeaf components by Michelle L. Wu**

Every project below opens a public page with its purpose, current behavior, an actual synthetic request/result, integration relationships, validation and next work. You do not need access to the private implementation repositories to read these pages.

Start with [Knowledge retrieval](projects/luxleaf-knowledge.md), [Usage metering](projects/luxleaf-metering.md), or [Workflow queue](projects/luxleaf-workflows.md).

## Business knowledge

| Public project page | What it does |
|---|---|
| [Workspace membership](projects/luxleaf-workspace.md) | Decide whether a workspace member may read, edit or manage business information. |
| [Knowledge retrieval](projects/luxleaf-knowledge.md) | Find an authorized policy passage that answers a team member’s question. |
| [Inference engine](projects/luxleaf-inference.md) | Return inspectable source excerpts when a local answer is sufficient. |
| [Prompt construction](projects/luxleaf-generation.md) | Prepare a bounded question-and-evidence message for a later model adapter. |
| [Knowledge orchestration](projects/luxleaf-rag.md) | Connect retrieval and inference while checking tenant identity and evidence excerpts. |
| [API boundary](projects/luxleaf-api.md) | Derive tenant context from authenticated host credentials before calling a permitted operation. |

## Governance and workflow

| Public project page | What it does |
|---|---|
| [Usage metering](projects/luxleaf-metering.md) | Reserve estimated usage before a request and keep uncertain spending visible. |
| [Workflow queue](projects/luxleaf-workflows.md) | Keep approved work durable while distinguishing queued, running and uncertain execution. |
| [Model routing](projects/luxleaf-model-router.md) | Choose an eligible model proposal within a tenant’s region and budget policy. |
| [Retrieval evaluation](projects/luxleaf-evaluations.md) | Measure retrieval results against a small set of explicitly labeled expectations. |
| [Model release governance](projects/luxleaf-model-governance.md) | Decide whether a particular model artifact has the required independent approvals. |
| [Model registry](projects/luxleaf-model-lifecycle.md) | Maintain a candidate registry and promote an approved artifact that meets a quality gate. |

## Agents and tools

| Public project page | What it does |
|---|---|
| [Agent planning](projects/luxleaf-agent-plans.md) | Review tool steps and dependencies before an execution runtime receives them. |
| [Tool protocol](projects/luxleaf-tool-protocol.md) | Expose a small, explicit local tool catalog with checked arguments. |
| [Cloud action policy](projects/luxleaf-cloud-tools.md) | Decide whether an inventory action fits an account and resource policy. |
| [Agent execution](projects/luxleaf-agent-runtime.md) | Execute a bounded sequence of registered local tools and retain its outcome. |

## Infrastructure and delivery

| Public project page | What it does |
|---|---|
| [Environment policy](projects/luxleaf-environments.md) | Review deployment requirements before an operator creates infrastructure. |
| [Batch scheduling](projects/luxleaf-batch.md) | Fit proposed jobs into a supplied CPU and memory capacity snapshot. |
| [Service runtime](projects/luxleaf-runtime.md) | Prepare restricted workload and service definitions for an operator to review. |
| [Data migrations](projects/luxleaf-data.md) | Plan additive data changes and provide transactional migration and backup utilities. |
| [Developer tooling](projects/luxleaf-developer-kit.md) | Determine a reproducible build order for a closed component dependency graph. |
| [Service authorization](projects/luxleaf-service-policy.md) | Make an explicit allow-or-deny decision for a service action and tenant. |
| [Release rollouts](projects/luxleaf-rollouts.md) | Use observation thresholds to propose holding, promoting or rolling back a candidate. |
| [Release delivery](projects/luxleaf-delivery.md) | Build a content-hash manifest and evaluate the required release-check assertions. |
| [Container deployment](projects/luxleaf-containers.md) | Prepare a restricted local container-service definition for a supplied image. |

## Operational evidence

| Public project page | What it does |
|---|---|
| [Event outbox](projects/luxleaf-events.md) | Retain operational events until each consumer acknowledges its own delivery. |
| [Evidence archives](projects/luxleaf-archives.md) | Keep a local chain of event records whose contents can be checked against a retained digest. |
| [Security posture](projects/luxleaf-security.md) | Identify missing deployment controls and show a concrete remediation for each. |
| [Telemetry privacy](projects/luxleaf-telemetry.md) | Prepare bounded operational metadata while dropping unapproved content fields. |
| [Service objectives](projects/luxleaf-observability.md) | Calculate request-window availability, latency percentiles and budget consumption. |
| [Incident response](projects/luxleaf-incidents.md) | Record an owner’s progress through a defined incident-response lifecycle. |

## What is public and what is private

This public repository contains the project pages, synthetic demonstrations, architecture and validation summaries. The 31 implementation repositories remain private. Public navigation deliberately stays within the public showcase.

The components are working local development releases. Several infrastructure projects generate plans or manifests; they do not create cloud infrastructure. All 31 private GitHub test workflows passed, alongside 129 local component tests and 6 portfolio integration tests. [Validation details](VALIDATION.md).

The earlier v0.3 integrated application is a separate demonstration; its screenshots and provider adapters must not be attributed to every new component. [Platform overview](PRODUCT.md).
