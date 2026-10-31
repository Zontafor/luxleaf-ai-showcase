# Protocols and integration roadmap

**Platform snapshot:** private v0.3 development foundation · **Evidence date:** October 30, 2026

This map gives every one of the 31 reviewed repositories a concrete relationship to LuxLeaf. It distinguishes implemented connections from the next substantive extension. It does not imply that every upstream application, workshop, notebook, or infrastructure stack has been recreated.

## New in v0.3

| Addition | Current behavior | Validation boundary |
|---|---|---|
| Tenant capability discovery | Clients can inspect their role's operations, supported workflow type, limits and service/protocol versions | Authenticated configuration snapshot, not a live provider health check |
| Tenant model catalog | Lists permitted aliases and bounded readiness reasons without exposing provider destinations or secrets | Execution still checks policy and configuration |
| Native JSON workflow interface | Shares admission, queue and submission identity with the existing multipart interface | One approved knowledge-query operation; full WES conformance is not claimed |
| Private async Python client | Discovery, queries and workflow lifecycle with explicit request identities and sanitized errors | No automatic paid retries; client code remains private |
| Expanded MCP bridge | Eight tools by default; workflow submission and cancellation added only when explicitly enabled | Remote work needs additional provider/tenant permission; external host validation remains ahead |
| S3 metadata archive adapter | Conditional object creation, bounded envelope checks, conflict verification and independent delivery receipts | Controlled SDK tests only; no live bucket, IAM policy, retention or immutable archive validation |

The S3 integration is separately opt-in and operator-controlled. It requires a preconfigured bucket and explicit expected owner, checks bucket public-access-block settings, and preserves uncertainty until delivery can be acknowledged. It does not create cloud resources. Changes to infrastructure policy, loss after acknowledgement, throughput, retention, and remote monitoring still require deployment work. Sending operational metadata to S3 can incur charges even when remote model inference is disabled.

## Example development

The [workflow protocol example](../examples/workflow-protocol.md) shows the public contract without exposing implementation code or credentials. The private implementation also includes an executable Python walkthrough: discovery is the default, and adding a local query/workflow requires an explicit execution option and stable request identity. Its localhost smoke run completed a synthetic workflow with citations and zero recorded model cost.

## Repository-by-repository map

| Reference | Area | Current LuxLeaf connection | Next substantive extension |
|---|---|---|---|
| [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | Application | Tenant API, console, roles, native workflow routes and client | SSO, membership lifecycle and target-platform delivery |
| [azure-search-openai-demo](https://github.com/azure-samples/azure-search-openai-demo) | Knowledge | Tenant lexical retrieval, source passages and Azure adapter | Hybrid retrieval, ingestion pipeline and representative quality evaluation |
| [sample-ai-gateway-for-amazon-bedrock](https://github.com/aws-samples/sample-ai-gateway-for-amazon-bedrock) | Gateway | Bedrock adapter behind common admission/accounting | Live identity and provider contract validation |
| [guidance-for-a-multi-tenant-generative-ai-gateway-with-cost-and-usage-tracking-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-a-multi-tenant-generative-ai-gateway-with-cost-and-usage-tracking-on-aws) | Governance | Tenant credit holds, rates, ledger and replay protection | Billing-period budgets and independent invoice reconciliation |
| [workflow-execution-service-schemas](https://github.com/ga4gh/workflow-execution-service-schemas) | Workflows | Legacy form subset plus native JSON workflow API | General engine adapter and independent WES conformance validation |
| [microsoft-foundry-baseline](https://github.com/Azure-Samples/microsoft-foundry-baseline) | Private deployment | Private manifest generator and explicit provider configuration | Azure private endpoints, workload identity and zone validation |
| [vertex-ai-samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples) | Evaluation | Synthetic retrieval gate and Vertex integration boundary | Training/registry lifecycle only after defining a model-owning workload |
| [sample-bedrock-ai-gateway](https://github.com/aws-samples/sample-bedrock-ai-gateway) | Gateway | Provider discovery and common tenant gateway | OIDC ingress, model-specific policy and load tests |
| [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | Models | Google text generation adapter with accounted usage | Live model evaluation and additional modalities if required |
| [azure-ai-agents-playbook](https://github.com/Azure-Samples/azure-ai-agents-playbook) | Agent design | Conceptual comparison only; no code/prose reuse | Resolve licensing before reuse; original host approval/evaluation designs |
| [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | MCP | Official SDK plus eight default tools and two opt-in workflow tools | External host acceptance and client-specific approval verification |
| [mcp](https://github.com/awslabs/mcp) | AWS tools | Narrow tenant tools; broad AWS toolkits not installed | Select only required AWS actions and define scoped identities |
| [agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | Agent integration | Typed tenant client and controlled tool access | Sandboxed, policy-limited service adapters per actual workflow |
| [amazon-bedrock-samples](https://github.com/aws-samples/amazon-bedrock-samples) | Model patterns | Converse adapter, lexical RAG and synthetic examples | Representative answer evaluation before agentic expansion |
| [regulated-mlops-using-amazon-sagemaker](https://github.com/aws-samples/regulated-mlops-using-amazon-sagemaker) | Release evidence | Source provenance, test gates and synthetic evaluation | Model registry, approval records and drift tests if training is introduced |
| [aws-batch-blueprints](https://github.com/aws-samples/aws-batch-blueprints) | Compute | Independent bounded workflow worker | Isolated Batch job adapter, resource policy and cancellation semantics |
| [serverless-patterns](https://github.com/aws-samples/serverless-patterns) | Events | Transactional event creation and retry-safe deliveries | Event consumers, backpressure and deliberate retry/dead-letter design |
| [ecs-blue-green-deployment](https://github.com/aws-samples/ecs-blue-green-deployment) | Promotion | Staging/rollback documentation and pinned-image manifests | Actual traffic switching and rollback rehearsal |
| [aws-eks-samples](https://github.com/aws-samples/aws-eks-samples) | Containers | Private Kubernetes manifests with resource/network boundaries | CNI, cluster, database and runtime acceptance tests |
| [aws-dynamodb-kinesisfirehose-s3-ingestion](https://github.com/aws-samples/aws-dynamodb-kinesisfirehose-s3-ingestion) | Archive | S3 adapter with conditional object creation and delivery receipts | Streaming delivery and retention policy; no DynamoDB/Firehose stack |
| [amazon-rds-purpose-built-workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop) | Storage | Relational accounting/queue consistency tested on PostgreSQL | Managed database, pooling, restore and capacity validation |
| [sample-aws-developer-project](https://github.com/aws-samples/sample-aws-developer-project) | Developer experience | Native API discovery, Python client and local walkthrough | Role-specific onboarding and deployment developer workflow |
| [serverless-samples](https://github.com/aws-samples/serverless-samples) | API lifecycle | Shared authenticated JSON/form contracts and tests | Environment-specific API front door and CI/CD provisioning |
| [amazon-vpc-lattice-blueprints](https://github.com/aws-samples/amazon-vpc-lattice-blueprints) | Service boundaries | Private service and network-policy manifest design | Lattice or mesh only if justified by service topology |
| [aws-security-reference-architecture-examples](https://github.com/aws-samples/aws-security-reference-architecture-examples) | Security operations | Tenant controls, private deployment boundaries and runbook | Account-level evidence, centralized policies and security review |
| [sample-otel-cloudwatch-no-collector](https://github.com/aws-samples/sample-otel-cloudwatch-no-collector) | Telemetry | Opt-in OTLP metadata traces | Collector delivery and any required signed cloud export |
| [sample-ac-e2e-observability](https://github.com/aws-samples/sample-ac-e2e-observability) | Observability | API/gateway traces, request IDs and operational counts | Queue age, worker health and agreed SLOs |
| [aws-incident-response-playbooks](https://github.com/aws-samples/aws-incident-response-playbooks) | Incident response | Original runbook, suspension, revocation and reconciliation | Restore and credential-incident exercises with named owners |
| [aws-codepipeline-cicd](https://github.com/aws-samples/aws-codepipeline-cicd) | CI | Local verification gate and private source bundle manifests | Controlled remote private-code build pipeline and artifact attestations |
| [amazon-ecs-fargate-cdk-v2-cicd](https://github.com/aws-samples/amazon-ecs-fargate-cdk-v2-cicd) | Container release | Container build definition and release boundaries | Fargate/IAM/registry deployment with live rollback validation |
| [mlops-e2e](https://github.com/aws-samples/mlops-e2e) | Lifecycle evaluation | Original synthetic retrieval evaluation and release gates | Workload-specific model lifecycle rather than importing an unauthenticated sample API |

## Sequence and acceptance

1. Validate one deployment runtime and one provider with synthetic data and bounded spending before increasing integration breadth.
2. Add individual-user identity and finer document permissions before broad team access.
3. Expand ingestion and retrieval against representative, authorized evaluation data.
4. Validate archive delivery monitoring, restore behavior, queue age and worker health before increasing autonomous execution.
5. Add domain-specific compute or model lifecycle services only after specifying the workload, permissions, resource limits and recovery behavior.

The private v0.3 suite recorded **81 passing tests with SQLite and the same 81 with PostgreSQL**. New checks cover protocol compatibility, client errors, tool opt-in, tenant isolation, archive request contracts, concurrent delivery, conflict handling and recovery after an uncertain write. These results do not establish live cloud operation or production capacity. See [validation](VALIDATION.md) and the [proposed release gates](TECHNICAL_BRIEF.md#proposed-release-gates).

Original LuxLeaf implementation remains private and proprietary. The showcase publishes this capability map and illustrative interface only. Reference projects retain their licenses; code and prose from the unlicensed agents playbook remain excluded. [References and attribution](REFERENCES.md).
