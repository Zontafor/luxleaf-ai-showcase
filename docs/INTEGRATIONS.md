# LuxLeaf component portfolio

Michelle L. Wu’s original LuxLeaf projects have been implemented as 31 separate private GitHub repositories. Each has a defined responsibility and an explicit integration boundary. The existing v0.3 application remains a separate development demonstration.

| Project | Responsibility | Further development |
|---|---|---|
| [luxleaf-workspace](https://github.com/Zontafor/luxleaf-workspace) | Persistent tenant memberships and role-based access decisions | Identity-provider login and a dedicated user interface |
| [luxleaf-knowledge](https://github.com/Zontafor/luxleaf-knowledge) | Persistent tenant documents, bounded passage retrieval and citations | Embedding search, document ACLs and binary document ingestion |
| [luxleaf-inference](https://github.com/Zontafor/luxleaf-inference) | Deterministic local extractive answers with tenant-bound evidence | Live model-provider adapters and provider-specific accounting |
| [luxleaf-metering](https://github.com/Zontafor/luxleaf-metering) | Durable credit reservations, replay checks and settlement | Provider invoice reconciliation and commercial billing |
| [luxleaf-workflows](https://github.com/Zontafor/luxleaf-workflows) | Durable tenant jobs with leases, fencing and cancellation | Isolated remote execution and distributed load validation |
| [luxleaf-environments](https://github.com/Zontafor/luxleaf-environments) | Validate deployment configuration against private-service requirements | Provisioning and live identity/network acceptance |
| [luxleaf-evaluations](https://github.com/Zontafor/luxleaf-evaluations) | Precision, recall and reciprocal-rank evaluation against labeled cases | Representative business datasets and answer-faithfulness evaluation |
| [luxleaf-model-router](https://github.com/Zontafor/luxleaf-model-router) | Deterministic selection by permissions, region, capacity and estimated cost | Live provider health and latency telemetry |
| [luxleaf-generation](https://github.com/Zontafor/luxleaf-generation) | Bounded literal templates and untrusted evidence delimiters | Model generation, tokenizer-specific budgeting and injection evaluation |
| [luxleaf-agent-plans](https://github.com/Zontafor/luxleaf-agent-plans) | Validate and order bounded tool plans with explicit approval requirements | An interactive plan review experience |
| [luxleaf-tool-protocol](https://github.com/Zontafor/luxleaf-tool-protocol) | Versioned JSON tool discovery and permission-checked invocation | MCP transport/host interoperability via a dedicated adapter |
| [luxleaf-cloud-tools](https://github.com/Zontafor/luxleaf-cloud-tools) | Evaluate narrowly scoped inventory actions against account/resource policy | Authenticated provider-specific execution adapters |
| [luxleaf-agent-runtime](https://github.com/Zontafor/luxleaf-agent-runtime) | Execute approved local tool plans with step budgets and explicit failure records | Durable execution checkpoints and process isolation |
| [luxleaf-rag](https://github.com/Zontafor/luxleaf-rag) | Compose tenant-filtered retrieval and local inference with verifiable citations | Live gateway integration and representative quality measurement |
| [luxleaf-model-governance](https://github.com/Zontafor/luxleaf-model-governance) | Evaluate release evidence and separation-of-duty approvals | Signed evidence and organization-specific compliance processes |
| [luxleaf-batch](https://github.com/Zontafor/luxleaf-batch) | Deterministic CPU/memory-constrained job placement with deferred-job reporting | Actual isolated compute execution and cluster scheduling |
| [luxleaf-events](https://github.com/Zontafor/luxleaf-events) | Durable deduplicated tenant events with consumer-specific acknowledgements | Leases, remote delivery and backpressure metrics |
| [luxleaf-rollouts](https://github.com/Zontafor/luxleaf-rollouts) | Canary promotion/rollback decisions using explicit observation gates | Actual traffic switching and deployment control |
| [luxleaf-runtime](https://github.com/Zontafor/luxleaf-runtime) | Generate restricted Kubernetes workload and service manifests | Cluster-side validation, images and live runtime acceptance |
| [luxleaf-archives](https://github.com/Zontafor/luxleaf-archives) | Local tenant event archive with chained hashes and tamper verification | Remote retention, signing and immutable storage |
| [luxleaf-data](https://github.com/Zontafor/luxleaf-data) | Transactional versioned SQLite migrations, backups and integrity checks | Managed PostgreSQL adapters and production restore exercises |
| [luxleaf-developer-kit](https://github.com/Zontafor/luxleaf-developer-kit) | Validate component dependency manifests and compute build order | Package registry distribution and developer onboarding UI |
| [luxleaf-api](https://github.com/Zontafor/luxleaf-api) | Tenant-bound authenticated in-process HTTP-style request dispatch | Production HTTP hosting, OIDC and edge throttling |
| [luxleaf-service-policy](https://github.com/Zontafor/luxleaf-service-policy) | Deny-by-default service-to-service action authorization | Workload identity verification and network enforcement |
| [luxleaf-security](https://github.com/Zontafor/luxleaf-security) | Deterministic deployment posture checks with actionable findings | Independent audit, threat testing and organization policy integration |
| [luxleaf-telemetry](https://github.com/Zontafor/luxleaf-telemetry) | Allowlisted bounded operational spans with tenant pseudonyms | Collector transport, key management and retention |
| [luxleaf-observability](https://github.com/Zontafor/luxleaf-observability) | Latency percentiles, availability and error-budget calculations | Live metric ingestion and alert delivery |
| [luxleaf-incidents](https://github.com/Zontafor/luxleaf-incidents) | Durable incident lifecycle with validated transitions and history | Notification integrations and staffed incident exercises |
| [luxleaf-delivery](https://github.com/Zontafor/luxleaf-delivery) | Content-addressed release manifests and mandatory validation gates | Signed artifacts and remote build/deployment execution |
| [luxleaf-containers](https://github.com/Zontafor/luxleaf-containers) | Generate restricted Compose service definitions from digest-pinned images | Image building/scanning and target-host acceptance |
| [luxleaf-model-lifecycle](https://github.com/Zontafor/luxleaf-model-lifecycle) | Durable candidate registration and evidence-gated model promotion | External model artifact storage, drift monitoring and rollback automation |

## Validation and delivery

The initial component suite passed **129 component tests, 6 cross-component integration tests and all 31 command-line examples** on Python 3.14.3. Input rejection, tenant boundaries, concurrent metering, transaction rollback and archive replay were exercised. Each repository has its own package, README, design/contract documentation, license, example, tests and CI definition. All 31 GitHub component test workflows passed on the uploaded commits. Private visibility, independent non-fork status and commit identity were verified for every repository.

All repositories are committed locally and uploaded privately to the approved Zontafor account. The repository links above require authorized GitHub access. This showcase does not distribute their source. These are bounded working components, not 31 deployed commercial applications. Several infrastructure projects generate plans or manifests only. No production deployment, live provider/storage call or business-scale performance is claimed.

The separate v0.3 integrated demonstration retains its own validation record. Its features and test results must not be assumed to exist in every new component. See [validation](VALIDATION.md).
