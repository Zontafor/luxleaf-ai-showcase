[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Container deployment

**luxleaf-containers · Infrastructure and delivery · Component 0.1.0**

Prepare a restricted local container-service definition for a supplied image.

## What works today

Generate restricted Compose service definitions from digest-pinned images.

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
    "name": "luxleaf-api",
    "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

**Recorded result**

```json
{
  "compose": {
    "name": "luxleaf-api",
    "services": {
      "luxleaf-api": {
        "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "user": "10001:10001",
        "read_only": true,
        "cap_drop": [
          "ALL"
        ],
        "security_opt": [
          "no-new-privileges:true"
        ],
        "pids_limit": 128,
        "mem_limit": "256m",
        "cpus": 0.5,
        "init": true,
        "restart": "unless-stopped",
        "ports": [
          "127.0.0.1:8080:8080"
        ],
        "tmpfs": [
          "/tmp:rw,noexec,nosuid,size=64m"
        ],
        "stop_grace_period": "30s"
      }
    }
  },
  "started": false
}
```

## Behavior and boundaries

Generate a Compose service for a supplied digest-pinned image. It runs under a numeric nonroot UID, uses a read-only root filesystem, drops capabilities, limits processes/memory/CPU and exposes its port on loopback only. A bounded temporary filesystem supports transient files.

The JSON compose object can be written as a Compose file. This does not build or start an image, provision a registry, configure application credentials or verify the image supports these restrictions. Service fields follow the [Compose service specification](https://docs.docker.com/reference/compose-file/services/). Review target-host behavior before deployment.

## Where it connects

[runtime](luxleaf-runtime.md) · [delivery](luxleaf-delivery.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Image building/scanning and target-host acceptance.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
