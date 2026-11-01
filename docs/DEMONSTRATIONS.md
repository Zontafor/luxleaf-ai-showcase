# Connected LuxLeaf demonstrations

**Five portfolio journeys plus one recovery exercise · All 31 components exercised · 39 executable checks passed across two records**

Explore how LuxLeaf components work together using synthetic business data. Each journey shows a flow, actual recorded results, rejected actions and the boundary between executed local behavior and unexecuted proposals. These are recorded demonstrations, not a live application or production measurements.

| Demonstration | What to inspect |
|---|---|
| [Knowledge with permission](demonstrations/knowledge-with-permission.md) | A permitted team member asks a policy question, with a budget hold and durable workflow. |
| [Controlled agent work](demonstrations/controlled-agent-work.md) | Plan two local text operations and evaluate a narrowly scoped cloud-inventory proposal. |
| [Evidence before release](demonstrations/evidence-before-release.md) | Evaluate synthetic retrieval results, review an artifact, and prepare a release manifest. |
| [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md) | Validate an environment, calculate placement, prepare runtime definitions, and exercise a local backup. |
| [Operational evidence and response](demonstrations/operational-evidence-and-response.md) | Archive a completion event, remove content from telemetry, calculate a service objective and record an incident exercise. |

## New: interrupted delivery recovery

[Follow the event/archive recovery exercise](demonstrations/event-delivery-recovery.md): a lease expires after an archive write, a reviewed replay preserves one entry, and the stale worker is rejected. The new exercise adds ten checks to the original five journeys' 29 checks.

## Start with a business question

[Knowledge with permission](demonstrations/knowledge-with-permission.md) follows one synthetic onboarding question from membership and authentication through retrieval, a budget reservation, local inference, workflow completion and settlement. It also shows rejected administrative access, tenant spoofing and excessive spending.

The other journeys demonstrate local agents, release decisions, deployment planning and operational evidence. The infrastructure and release steps produce reviewable proposals. The data journey additionally performs a real backup check on a disposable local database.

## Complete capability coverage

Every component below appears in at least one recorded execution step. These links open public evidence pages.

| Component | Demonstration evidence |
|---|---|
| [luxleaf-agent-plans](projects/luxleaf-agent-plans.md) | [Controlled agent work](demonstrations/controlled-agent-work.md#step-2) |
| [luxleaf-agent-runtime](projects/luxleaf-agent-runtime.md) | [Controlled agent work](demonstrations/controlled-agent-work.md#step-4) |
| [luxleaf-api](projects/luxleaf-api.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-2) |
| [luxleaf-archives](projects/luxleaf-archives.md) | [Operational evidence and response](demonstrations/operational-evidence-and-response.md#step-1) |
| [luxleaf-batch](projects/luxleaf-batch.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-2) |
| [luxleaf-cloud-tools](projects/luxleaf-cloud-tools.md) | [Controlled agent work](demonstrations/controlled-agent-work.md#step-6) |
| [luxleaf-containers](projects/luxleaf-containers.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-4) |
| [luxleaf-data](projects/luxleaf-data.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-5) |
| [luxleaf-delivery](projects/luxleaf-delivery.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-7) |
| [luxleaf-developer-kit](projects/luxleaf-developer-kit.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-6) |
| [luxleaf-environments](projects/luxleaf-environments.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-1) |
| [luxleaf-evaluations](projects/luxleaf-evaluations.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-1) |
| [luxleaf-events](projects/luxleaf-events.md) | [Operational evidence and response](demonstrations/operational-evidence-and-response.md#step-2) |
| [luxleaf-generation](projects/luxleaf-generation.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-7) |
| [luxleaf-incidents](projects/luxleaf-incidents.md) | [Operational evidence and response](demonstrations/operational-evidence-and-response.md#step-5) |
| [luxleaf-inference](projects/luxleaf-inference.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-8) |
| [luxleaf-knowledge](projects/luxleaf-knowledge.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-3) |
| [luxleaf-metering](projects/luxleaf-metering.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-11) |
| [luxleaf-model-governance](projects/luxleaf-model-governance.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-3) |
| [luxleaf-model-lifecycle](projects/luxleaf-model-lifecycle.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-4) |
| [luxleaf-model-router](projects/luxleaf-model-router.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-4) |
| [luxleaf-observability](projects/luxleaf-observability.md) | [Operational evidence and response](demonstrations/operational-evidence-and-response.md#step-4) |
| [luxleaf-rag](projects/luxleaf-rag.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-9) |
| [luxleaf-rollouts](projects/luxleaf-rollouts.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-6) |
| [luxleaf-runtime](projects/luxleaf-runtime.md) | [Deployment planning and recovery](demonstrations/deployment-planning-and-recovery.md#step-3) |
| [luxleaf-security](projects/luxleaf-security.md) | [Evidence before release](demonstrations/evidence-before-release.md#step-5) |
| [luxleaf-service-policy](projects/luxleaf-service-policy.md) | [Controlled agent work](demonstrations/controlled-agent-work.md#step-1) |
| [luxleaf-telemetry](projects/luxleaf-telemetry.md) | [Operational evidence and response](demonstrations/operational-evidence-and-response.md#step-3) |
| [luxleaf-tool-protocol](projects/luxleaf-tool-protocol.md) | [Controlled agent work](demonstrations/controlled-agent-work.md#step-3) |
| [luxleaf-workflows](projects/luxleaf-workflows.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-10) |
| [luxleaf-workspace](projects/luxleaf-workspace.md) | [Knowledge with permission](demonstrations/knowledge-with-permission.md#step-1) |

## How to read the evidence

- **Executed local component:** the recorded result came from the component’s actual Python implementation.
- **Executed negative case:** an invalid or prohibited request was made and rejected; unexpected acceptance stops the runner.
- **Synthetic assertions or samples:** the evaluator ran, but supplied reviews, controls, metrics, images or capacity are fixtures. They are not claims about a real deployment.

The run contains 29 passing checks. The original demonstration validation passed 9 portfolio tests, including a test that deliberately bypasses the budget rule and confirms the demonstration refuses to report success. Another test checks that recorded evidence excludes credential strings, lease tokens and private filesystem paths. These results are separate from the earlier 129 component tests. [Full validation record](VALIDATION.md).

[Download or inspect the recorded evidence](demonstrations/record.json) · [Browse individual project examples](INTEGRATIONS.md)

The October 31 expansion passed 143 component tests and 12 portfolio tests. The additional [recovery record](demonstrations/event-recovery-record.json) is separate from the preserved five-journey record.
