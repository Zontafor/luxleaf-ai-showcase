[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Data migrations

**luxleaf-data · Infrastructure and delivery · Component 0.1.0**

Plan additive data changes and provide transactional migration and backup utilities.

## What works today

Transactional versioned SQLite migrations, backups and integrity checks.

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
    "migrations": [
      {
        "version": 1,
        "table": "documents",
        "columns": {
          "id": "TEXT",
          "body": "TEXT"
        }
      }
    ]
  }
}
```

**Recorded result**

```json
{
  "target_version": 1,
  "pending_statements": [
    "CREATE TABLE \"documents\" (\"id\" TEXT, \"body\" TEXT)"
  ],
  "applied": false
}
```

## Behavior and boundaries

The JSON interface generates an additive migration plan from bounded table/column declarations. Identifiers and SQL types are allowlisted. The Python migrate function executes pending table creations and advances SQLite user_version in one transaction. Newer database versions are rejected; an error rolls back all pending changes.

The backup function uses SQLite's online backup API into an exclusively created destination and runs integrity_check. It refuses overwrite. Migration sets must be retained unchanged; this initial version does not hash applied migration definitions or support destructive changes. Paths are supplied by trusted operator code, never by remote requests.

## Where it connects

[knowledge](luxleaf-knowledge.md) · [workflows](luxleaf-workflows.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 6 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Managed PostgreSQL adapters and production restore exercises.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
