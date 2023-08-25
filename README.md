# copy-ingress-resources-from-v1Beta-to-k8s.io-v1
Kubernetes Ingress API version networking.k8s.io/v1 has lot of changes in fields wrt extensions/v1beta1 like the following:

* `spec.backend` -> `spec.defaultBackend`
* `serviceName` -> `service.name`
* `servicePort` -> `service.port.name` (for string values)
* `servicePort` -> `service.port.number` (for numeric values)
* `pathType` no longer has a default value in v1; "Exact", "Prefix", or "ImplementationSpecific" must be specified

This scripts basically copy all ingress resources from a cluster using v1beta1 apis and modify all the resources to be compatiable with networking.k8s.io/v1.
