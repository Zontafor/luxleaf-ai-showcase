# Roadmap

For proposed release gates and the evidence each stage requires, read the [Product & Technical Brief](TECHNICAL_BRIEF.md).

This roadmap describes development priorities. It is not a commitment to release dates or contractual availability.

| Stage | Scope | Evidence required |
|---|---|---|
| Implemented development foundation | Tenant API keys and roles, text retrieval, governed inference, durable knowledge-query jobs, MCP bridge, metadata events | Recorded v0.2 tests and synthetic demonstrations; see VALIDATION.md |
| Deployment validation | Reproducible container builds, private staging deployment, workload identity, live provider contract checks | Successful staging runs, provider accounting checks, secret/dependency review |
| Business access and knowledge | Individual-user SSO, membership lifecycle, finer document permissions, asynchronous ingestion, hybrid retrieval | Cross-tenant and per-document authorization tests; representative retrieval evaluation |
| Operational maturity | Restore exercises, worker health and queue-age signals, remote event archive, retention controls | Measured recovery targets, failure exercises, delivery and retention validation |
| Commercial readiness | Billing integration, billing-period budgets, invoice reconciliation, customer onboarding | End-to-end billing and access tests; reviewed customer terms and support processes |
| Additional workflows | Allowlisted domain-specific execution adapters and isolated job runners | Workload-specific resource, identity, data, and result validation |

## Not currently claimed

Production-scale performance, multi-region availability, general scientific workflow execution, full GA4GH WES conformance, regulated-domain suitability, and security/compliance certifications have not been established.

Feature requests should describe a concrete business task, its constraints, and a measurable successful outcome. Please use synthetic examples in public discussions.
