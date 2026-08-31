# Grafana Dashboard

## Overview

Pulse uses Grafana to provide a visual representation of infrastructure health metrics collected by Prometheus.

The dashboard transforms raw monitoring metrics into clear visualisations, providing an at-a-glance view of CPU usage, memory usage, disk usage, and system uptime.

Grafana uses Prometheus as its data source, while Prometheus collects metrics exposed through the Pulse FastAPI `/metrics` endpoint.

---

## Dashboard Architecture

```text
Pulse
  │
  ▼
FastAPI /metrics
  │
  │ scrape
  ▼
Prometheus
  │
  │ query
  ▼
Grafana
  │
  ▼
Infrastructure Dashboard
```

This separates metric collection from visualisation:

- Pulse collects and exposes system metrics.
- Prometheus scrapes and stores the metrics.
- Grafana queries Prometheus and presents the data through dashboard panels.

---

## Dashboard Panels

The current Pulse dashboard provides four core infrastructure metrics.

| Panel | Description |
| --- | --- |
| CPU Usage | Current processor utilisation |
| Memory Usage | Current system memory utilisation |
| Disk Usage | Current disk utilisation |
| System Uptime | Current system uptime |

Together, these panels provide a concise overview of the monitored system's resource usage and availability.

---

## CPU Usage

The CPU panel displays current processor utilisation as a percentage.

This provides visibility into:

- Current system load
- High CPU utilisation
- Resource pressure

Example monitoring thresholds:

| Status | Usage |
| --- | ---: |
| Normal | Below 80% |
| Warning | 80–89% |
| Critical | 90% and above |

Actual alert thresholds are controlled through Pulse configuration.

---

## Memory Usage

The memory panel displays current system memory utilisation.

Monitoring memory usage provides visibility into:

- Current memory consumption
- Memory pressure
- Potential resource exhaustion

Example monitoring thresholds:

| Status | Usage |
| --- | ---: |
| Normal | Below 80% |
| Warning | 80–89% |
| Critical | 90% and above |

Actual alert thresholds are controlled through Pulse configuration.

---

## Disk Usage

The disk panel displays current disk utilisation.

Monitoring disk usage provides visibility into:

- Current storage utilisation
- Low available disk capacity
- Potential resource constraints

Example monitoring thresholds:

| Status | Usage |
| --- | ---: |
| Normal | Below 85% |
| Warning | 85–94% |
| Critical | 95% and above |

Actual alert thresholds are controlled through Pulse configuration.

---

## System Uptime

The uptime panel displays system uptime.

This metric provides additional operational context when monitoring the environment and can help identify unexpected system restarts.

---

## Data Source

Grafana retrieves Pulse monitoring data from Prometheus.

The Prometheus data source is available within the Docker Compose network at:

```text
http://prometheus:9090
```

This uses the Docker Compose service name rather than `localhost`, allowing the Grafana container to communicate directly with the Prometheus container.

---

## Metric Collection

Pulse exposes Prometheus-compatible metrics through the FastAPI:

```text
/metrics
```

The monitoring flow is:

```text
System Resources
       │
       ▼
     Pulse
       │
       ▼
FastAPI /metrics
       │
       │ scraped by
       ▼
   Prometheus
       │
       │ queried by
       ▼
     Grafana
```

Prometheus periodically scrapes the endpoint and stores the resulting metric data.

Grafana queries Prometheus to populate the infrastructure dashboard.

---

## Dashboard Persistence

Grafana uses persistent Docker storage.

This allows Grafana configuration and dashboard state to remain available across container restarts.

Persistent storage helps retain:

- Dashboard configuration
- Data source configuration
- Dashboard customisations

The persistent volume is managed through the Pulse Docker Compose configuration.

---

## Accessing Grafana

When running the complete monitoring stack with Docker Compose, Grafana is available locally at:

```text
http://localhost:3000
```

If the local development environment uses the default Grafana credentials:

```text
Username: admin
Password: admin
```

Default credentials should only be used for local development and should be changed before using the stack in a less restricted environment.

---

## Dashboard Screenshot

A screenshot of the current Pulse Grafana dashboard is stored at:

```text
screenshots/grafana-dashboard.png
```

The dashboard includes panels for:

- CPU usage
- Memory usage
- Disk usage
- System uptime

This screenshot is also used to demonstrate the observability layer within the repository and portfolio.

---

## Current Dashboard Scope

The current Grafana dashboard is intentionally focused on the four core metrics exposed by Pulse:

```text
CPU
Memory
Disk
Uptime
```

This dashboard represents the completed Grafana scope for the current Pulse monitoring platform.

The objective is to provide a clear infrastructure overview without expanding the project into a larger monitoring or incident-management product.

---

## Maintenance

Future Grafana work is limited primarily to maintaining and improving the existing dashboard.

Maintenance may include:

- Fixing broken queries or panels
- Updating dashboard configuration
- Improving panel readability
- Maintaining Prometheus compatibility
- Updating Grafana versions
- Reviewing persistent storage configuration
- Updating screenshots and documentation
- Small visual or operational improvements

Additional monitoring domains such as multi-host monitoring, container orchestration monitoring, incident timelines, and large-scale infrastructure dashboards are outside the current Pulse scope.

---

## Design Principles

### Simplicity

The dashboard focuses on the core infrastructure metrics required to understand the monitored system's current health.

### Readability

Panels should present monitoring information clearly and make abnormal resource usage easy to identify.

### Operational Awareness

The dashboard complements Pulse's health endpoint, structured logs, and alerting system by providing a visual view of infrastructure metrics.

### Maintainability

Dashboard configuration should remain straightforward to run, understand, and maintain alongside the existing Prometheus monitoring stack.

---

## Related Documentation

- [Architecture](./architecture.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Alerting](./alerting.md)
- [Configuration](./configuration.md)
- [Roadmap](./roadmap.md)