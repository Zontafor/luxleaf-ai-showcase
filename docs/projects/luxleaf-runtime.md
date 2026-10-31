[Browse all projects](../INTEGRATIONS.md) · [LuxLeaf overview](../../README.md)

# Service runtime

**luxleaf-runtime · Infrastructure and delivery · Component 0.1.0**

Prepare restricted workload and service definitions for an operator to review.

## What works today

Generate restricted Kubernetes workload and service manifests.

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
    "namespace": "luxleaf",
    "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

**Recorded result**

```json
{
  "manifests": [
    {
      "apiVersion": "apps/v1",
      "kind": "Deployment",
      "metadata": {
        "name": "luxleaf-api",
        "namespace": "luxleaf"
      },
      "spec": {
        "replicas": 2,
        "selector": {
          "matchLabels": {
            "app.kubernetes.io/name": "luxleaf-api"
          }
        },
        "template": {
          "metadata": {
            "labels": {
              "app.kubernetes.io/name": "luxleaf-api"
            }
          },
          "spec": {
            "automountServiceAccountToken": false,
            "securityContext": {
              "runAsNonRoot": true,
              "runAsUser": 10001,
              "runAsGroup": 10001,
              "seccompProfile": {
                "type": "RuntimeDefault"
              }
            },
            "containers": [
              {
                "name": "luxleaf-api",
                "image": "registry.example/luxleaf@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ports": [
                  {
                    "containerPort": 8080
                  }
                ],
                "securityContext": {
                  "allowPrivilegeEscalation": false,
                  "readOnlyRootFilesystem": true,
                  "capabilities": {
                    "drop": [
                      "ALL"
                    ]
                  }
                },
                "resources": {
                  "requests": {
                    "cpu": "250m",
                    "memory": "256Mi"
                  },
                  "limits": {
                    "cpu": "250m",
                    "memory": "256Mi"
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "apiVersion": "v1",
      "kind": "Service",
      "metadata": {
        "name": "luxleaf-api",
        "namespace": "luxleaf"
      },
      "spec": {
        "type": "ClusterIP",
        "selector": {
          "app.kubernetes.io/name": "luxleaf-api"
        },
        "ports": [
          {
            "port": 8080,
            "targetPort": 8080
          }
        ]
      }
    }
  ],
  "applied": false
}
```

## Behavior and boundaries

Generate a Deployment and internal ClusterIP Service with matching selectors, bounded resource requests/limits, a digest-pinned image, nonroot identity, default seccomp, dropped Linux capabilities and a read-only root filesystem. Service-account token mounting is disabled.

These are manifest objects only. The image must support the chosen UID, filesystem and port. Namespace creation, secrets, readiness probes, egress policy, database connectivity, admission and cluster-side validation remain deployment work. Field semantics follow the [Kubernetes pod security documentation](https://kubernetes.io/docs/concepts/security/pod-security-standards/); no cluster deployment is performed.

## Where it connects

[environments](luxleaf-environments.md) · [containers](luxleaf-containers.md)

These links open other public project pages. The portfolio integration tests demonstrate selected connections; this relationship list does not claim that every connection is deployed.

## Validation and next work

- 4 component tests passed locally. This component’s private GitHub test workflow also passed on its uploaded commit.
- The full portfolio recorded 129 component tests, 6 integration tests and 31 command-line examples. This page’s synthetic example was executed separately when preparing the public documentation.
- Further development: Cluster-side validation, images and live runtime acceptance.

No live cloud acceptance, production capacity, independent security assurance or compliance certification is claimed. See the [validation record](../VALIDATION.md) for the evidence boundary.

Copyright © 2026 Michelle L. Wu. Public materials are governed by the [showcase license](../../LICENSE); it does not grant access to private source.
