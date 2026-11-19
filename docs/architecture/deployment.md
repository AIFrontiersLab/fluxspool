# Deployment

```mermaid
flowchart LR
    lb[Ingress / load balancer] --> svc[Service]
    svc --> p1[tokenizer-design-lab pod 1]
    svc --> p2[tokenizer-design-lab pod 2]
    svc --> p3[tokenizer-design-lab pod N]
    hpa[HorizontalPodAutoscaler] -. scales .-> p1
    cm[(ConfigMap: TOML profile)] -.-> p1
    prom[(Prometheus)] -. scrapes /metrics .-> svc
    pvc[(Volume: jsonl runs + audit)] -.-> p1
```

- Stateless replicas behind a Service; scale on CPU via HPA.
- Configuration is a TOML profile mounted from a ConfigMap and selected with `TOKENIZER_DESIGN_LAB_CONFIG`.
- Readiness uses `/readyz`; liveness uses `/healthz`.
- PodDisruptionBudget keeps at least one replica during voluntary disruptions.
- NetworkPolicy allows ingress only from the gateway namespace.
