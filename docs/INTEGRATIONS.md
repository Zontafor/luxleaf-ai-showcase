# LuxLeaf component portfolio

Michelle L. Wu’s original LuxLeaf projects are being developed as separate private repositories. Each has a defined responsibility and an explicit integration boundary. The existing v0.3 application remains a separate development demonstration.

| Project | Responsibility | Further development |
|---|---|---|
| luxleaf-workspace | Persistent tenant memberships and role-based access decisions | Identity-provider login and a dedicated user interface |
| luxleaf-knowledge | Persistent tenant documents, bounded passage retrieval and citations | Embedding search, document ACLs and binary document ingestion |
| luxleaf-inference | Deterministic local extractive answers with tenant-bound evidence | Live model-provider adapters and provider-specific accounting |
| luxleaf-metering | Durable credit reservations, replay checks and settlement | Provider invoice reconciliation and commercial billing |
| luxleaf-workflows | Durable tenant jobs with leases, fencing and cancellation | Isolated remote execution and distributed load validation |
| luxleaf-environments | Validate deployment configuration against private-service requirements | Provisioning and live identity/network acceptance |
| luxleaf-evaluations | Precision, recall and reciprocal-rank evaluation against labeled cases | Representative business datasets and answer-faithfulness evaluation |
| luxleaf-model-router | Deterministic selection by permissions, region, capacity and estimated cost | Live provider health and latency telemetry |
| luxleaf-generation | Bounded literal templates and untrusted evidence delimiters | Model generation, tokenizer-specific budgeting and injection evaluation |
| luxleaf-agent-plans | Validate and order bounded tool plans with explicit approval requirements | An interactive plan review experience |
| luxleaf-tool-protocol | Versioned JSON tool discovery and permission-checked invocation | MCP transport/host interoperability via a dedicated adapter |
| luxleaf-cloud-tools | Evaluate narrowly scoped inventory actions against account/resource policy | Authenticated provider-specific execution adapters |
| luxleaf-agent-runtime | Execute approved local tool plans with step budgets and explicit failure records | Durable execution checkpoints and process isolation |
| luxleaf-rag | Compose tenant-filtered retrieval and local inference with verifiable citations | Live gateway integration and representative quality measurement |
| luxleaf-model-governance | Evaluate release evidence and separation-of-duty approvals | Signed evidence and organization-specific compliance processes |
| luxleaf-batch | Deterministic CPU/memory-constrained job placement with deferred-job reporting | Actual isolated compute execution and cluster scheduling |
| luxleaf-events | Durable deduplicated tenant events with consumer-specific acknowledgements | Leases, remote delivery and backpressure metrics |
| luxleaf-rollouts | Canary promotion/rollback decisions using explicit observation gates | Actual traffic switching and deployment control |
| luxleaf-runtime | Generate restricted Kubernetes workload and service manifests | Cluster-side validation, images and live runtime acceptance |
| luxleaf-archives | Local tenant event archive with chained hashes and tamper verification | Remote retention, signing and immutable storage |
| luxleaf-data | Transactional versioned SQLite migrations, backups and integrity checks | Managed PostgreSQL adapters and production restore exercises |
| luxleaf-developer-kit | Validate component dependency manifests and compute build order | Package registry distribution and developer onboarding UI |
| luxleaf-api | Tenant-bound authenticated in-process HTTP-style request dispatch | Production HTTP hosting, OIDC and edge throttling |
| luxleaf-service-policy | Deny-by-default service-to-service action authorization | Workload identity verification and network enforcement |
| luxleaf-security | Deterministic deployment posture checks with actionable findings | Independent audit, threat testing and organization policy integration |
| luxleaf-telemetry | Allowlisted bounded operational spans with tenant pseudonyms | Collector transport, key management and retention |
| luxleaf-observability | Latency percentiles, availability and error-budget calculations | Live metric ingestion and alert delivery |
| luxleaf-incidents | Durable incident lifecycle with validated transitions and history | Notification integrations and staffed incident exercises |
| luxleaf-delivery | Content-addressed release manifests and mandatory validation gates | Signed artifacts and remote build/deployment execution |
| luxleaf-containers | Generate restricted Compose service definitions from digest-pinned images | Image building/scanning and target-host acceptance |
| luxleaf-model-lifecycle | Durable candidate registration and evidence-gated model promotion | External model artifact storage, drift monitoring and rollback automation |

Implementation and validation status will be recorded after the independent component suite is verified. No production deployment or live cloud acceptance is claimed.
