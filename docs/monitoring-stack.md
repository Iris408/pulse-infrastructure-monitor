# Monitoring Stack

## Overview

This document explains the monitoring and observability stack used by Pulse.

The stack combines:

- FastAPI `/health` endpoint
- FastAPI `/metrics` endpoint
- Prometheus metric collection
- Grafana dashboard visualisation
- Docker Compose services
- Prometheus data source configuration
- Dashboard configuration

Together, these components provide health reporting, metric collection, and infrastructure visualisation for the monitored system.

---

## Architecture

```text
System Resources
       │
       ▼
     Pulse
       │
       ├──────────────► /health
       │
       └──────────────► /metrics
                            │
                            │ scrape
                            ▼
                       Prometheus
                            │
                            │ query
                            ▼
                         Grafana
```

Pulse collects system resource information and exposes operational data through FastAPI.

Prometheus periodically scrapes the `/metrics` endpoint and stores the resulting time-series metrics.

Grafana uses Prometheus as its data source to provide infrastructure dashboard visualisations.

---

## Services

When running locally, the monitoring stack is available through the following services:

| Service | URL |
| --- | --- |
| API Root | `http://localhost:8000` |
| Health Endpoint | `http://localhost:8000/health` |
| Metrics Endpoint | `http://localhost:8000/metrics` |
| Swagger UI | `http://localhost:8000/docs` |
| Prometheus | `http://localhost:9090` |
| Grafana | `http://localhost:3000` |

---

## FastAPI

FastAPI provides the operational HTTP interface for Pulse.

The monitoring stack primarily uses two endpoints:

```text
/health
/metrics
```

### Health Endpoint

The health endpoint can be checked locally with:

```bash
curl http://127.0.0.1:8000/health
```

The endpoint provides health information including:

- CPU
- Memory
- Disk
- Uptime
- Overall status

This provides a lightweight way to inspect the current health information exposed by Pulse.

---

### Metrics Endpoint

Prometheus-compatible metrics are exposed through:

```bash
curl http://127.0.0.1:8000/metrics
```

Current metrics include:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

These metrics form the connection between the Pulse monitoring application and Prometheus.

---

## Prometheus

Prometheus collects the metrics exposed by Pulse.

The scrape configuration is stored within the project's configuration structure:

```text
config/
└── prometheus.yml
```

Within the Docker Compose network, Prometheus scrapes the Pulse service using:

```text
monitor:8000
```

The monitoring relationship is:

```text
Prometheus
    │
    │ HTTP scrape
    ▼
monitor:8000/metrics
```

Prometheus is available locally at:

```text
http://localhost:9090
```

---

## Prometheus Target

The configured scrape target can be inspected through the Prometheus interface.

Navigate to:

```text
Status → Targets
```

The Pulse monitoring target should report:

```text
pulse-monitor UP
```

An `UP` target confirms that Prometheus can successfully reach and scrape the Pulse metrics endpoint.

---

## Prometheus Queries

Current Pulse metrics can be queried directly through Prometheus.

### CPU Usage

```text
system_cpu_usage_percent
```

### Memory Usage

```text
system_memory_usage_percent
```

### Disk Usage

```text
system_disk_usage_percent
```

### System Uptime

```text
system_uptime_hours
```

These metrics are also used by the Grafana dashboard.

---

## Grafana

Grafana provides the visualisation layer for the Pulse monitoring stack.

Grafana runs as part of the Docker Compose environment and connects to Prometheus as its data source.

Grafana is available locally at:

```text
http://localhost:3000
```

The default local development login is:

```text
Username: admin
Password: admin
```

Default credentials should only be used for local development.

---

## Prometheus Data Source

Within the Docker Compose network, Grafana connects to Prometheus using:

```text
http://prometheus:9090
```

Docker Compose service discovery allows Grafana to use the Prometheus service name directly.

The data flow is:

```text
Pulse
  │
  ▼
Prometheus
  │
  ▼
Grafana
```

---

## Grafana Dashboard

The current dashboard is named:

```text
Pulse Infrastructure Overview
```

It provides four core infrastructure panels:

| Panel | Prometheus Query | Visualisation |
| --- | --- | --- |
| CPU Usage | `system_cpu_usage_percent` | Gauge |
| Memory Usage | `system_memory_usage_percent` | Gauge |
| Disk Usage | `system_disk_usage_percent` | Gauge |
| System Uptime | `system_uptime_hours` | Stat |

The dashboard layout is:

```text
[ CPU Usage ]     [ Memory Usage ]

[ Disk Usage ]    [ System Uptime ]
```

This intentionally provides a concise overview of the core system metrics monitored by Pulse.

See [Grafana Dashboard](./grafana-dashboard.md) for more information.

---

## Docker Compose

The complete monitoring stack runs through Docker Compose.

Current services:

```text
monitor
prometheus
grafana
```

The service relationship is:

```text
┌──────────────────┐
│     monitor      │
│     FastAPI      │
│      :8000       │
└────────┬─────────┘
         │
         │ /metrics
         ▼
┌──────────────────┐
│    prometheus    │
│      :9090       │
└────────┬─────────┘
         │
         │ queries
         ▼
┌──────────────────┐
│     grafana      │
│      :3000       │
└──────────────────┘
```

---

## Running the Stack

### Build and Start

Start the complete monitoring stack:

```bash
docker compose up --build
```

### Background Mode

Run the services in the background:

```bash
docker compose up -d
```

### Check Services

Check the current container status:

```bash
docker compose ps
```

### Stop

Stop the monitoring stack:

```bash
docker compose down
```

---

## Grafana Persistence

Grafana uses the persistent Docker volume:

```text
grafana_data
```

This allows Grafana state to remain available across container restarts.

The persistent volume supports retention of:

- Grafana configuration
- Prometheus data source configuration
- Dashboard configuration
- Dashboard customisations

---

## Monitoring Responsibilities

Each component of the stack has a specific responsibility.

| Component | Responsibility |
| --- | --- |
| Pulse | Collect system metrics and expose operational endpoints |
| FastAPI | Provide `/health` and `/metrics` HTTP interfaces |
| Prometheus | Scrape and store time-series metrics |
| Grafana | Query and visualise Prometheus metrics |
| Docker Compose | Run and connect the monitoring services |

Keeping these responsibilities separate makes the stack easier to understand and maintain.

---

## Current Status

The core monitoring and observability stack is complete.

| Feature | Status |
| --- | --- |
| FastAPI `/health` endpoint | Complete |
| FastAPI `/metrics` endpoint | Complete |
| Prometheus scrape configuration | Complete |
| Prometheus metric collection | Complete |
| Grafana Docker service | Complete |
| Grafana persistent volume | Complete |
| CPU dashboard panel | Complete |
| Memory dashboard panel | Complete |
| Disk dashboard panel | Complete |
| System uptime dashboard panel | Complete |
| Docker Compose stack | Complete |

---

## Maintenance

The current monitoring stack represents the completed infrastructure scope for Pulse.

Future work is limited primarily to maintenance and reliability improvements, which may include:

- Automated endpoint and metric tests
- Docker configuration validation
- CI improvements
- Dependency and container image updates
- Security analysis
- Prometheus configuration maintenance
- Grafana compatibility maintenance
- Dashboard query fixes
- Configuration validation
- Documentation updates

Features such as alert-history storage, dedicated alert APIs, database-backed incident data, multi-host monitoring, and large-scale monitoring infrastructure are outside the current Pulse scope.

---

## Troubleshooting

If Prometheus cannot collect Pulse metrics:

1. Confirm the containers are running:

```bash
docker compose ps
```

2. Check the Pulse metrics endpoint:

```bash
curl http://127.0.0.1:8000/metrics
```

3. Open Prometheus:

```text
http://localhost:9090
```

4. Check:

```text
Status → Targets
```

5. Confirm the Pulse target reports:

```text
UP
```

If Grafana does not display data, confirm that its Prometheus data source is configured as:

```text
http://prometheus:9090
```

See [Troubleshooting](./troubleshooting.md) for additional diagnostic guidance.

---

## Related Documentation

- [Architecture](./architecture.md)
- [Alerting](./alerting.md)
- [Configuration](./configuration.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Logging](./logging.md)
- [Roadmap](./roadmap.md)
- [Setup](./setup.md)
- [Troubleshooting](./troubleshooting.md)