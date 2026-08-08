# Grafana Dashboard

## Overview

Pulse uses Grafana to provide a visual representation of system health metrics collected by Prometheus.

The dashboard transforms raw infrastructure metrics into easy-to-understand visualisations, allowing developers and operators to monitor application health at a glance.

Grafana is connected directly to Prometheus, which continuously pulls performance metrics from the Pulse FastAPI app.

---

## Dashboard Architecture

```text
Pulse Monitor
      │
      ▼
 /metrics Endpoint
      │
      ▼
 Prometheus
      │
      ▼
 Grafana
      │
      ▼
 Infrastructure Dashboard
```

---

## Dashboard Panels

The current dashboard provides four core infrastructure metrics.

| Panel | Description |
|---------|-------------|
| CPU Usage | Current processor utilisation |
| Memory Usage | Current system memory consumption |
| Disk Usage | Current disk utilisation |
| System Uptime | Total application uptime |

These panels provide a quick overview of the monitored system's health.

---

## CPU Usage

The CPU panel displays current processor utilisation as a percentage.

This metric helps identify:

- High system load
- CPU-intensive workloads
- Resource bottlenecks

Typical thresholds:

| Status | Usage |
|---------|------:|
| Normal | Below 80% |
| Warning | 80–89% |
| Critical | 90% and above |

---

## Memory Usage

The memory panel displays current RAM utilisation.

Monitoring memory usage helps identify:

- Memory pressure
- Potential leaks
- Resource exhaustion

Typical thresholds:

| Status | Usage |
|---------|------:|
| Normal | Below 80% |
| Warning | 80–89% |
| Critical | 90% and above |

---

## Disk Usage

The disk panel displays storage utilisation.

Monitoring disk capacity helps prevent:

- Full disks
- Application failures
- Logging interruptions

Typical thresholds:

| Status | Usage |
|---------|------:|
| Normal | Below 85% |
| Warning | 85–94% |
| Critical | 95% and above |

---

## System Uptime

The uptime panel shows how long the monitoring application has been running.

This metric provides visibility into:

- Service stability
- Unexpected restarts
- Deployment verification

A continuously increasing uptime generally indicates stable operation.

---

## Data Source

Grafana retrieves all monitoring data from Prometheus.

Default data source:

```text
Prometheus
```

Default connection:

```text
http://prometheus:9090
```

---

## Metric Collection

Pulse exposes metrics in a format Prometheus can read, via the `/metrics` endpoint on the FastAPI app.

Prometheus checks this endpoint at regular intervals and stores the data it collects.

Grafana then queries Prometheus to display that data as visualisations.

---

## Dashboard Persistence

Grafana dashboards are stored using a persistent Docker volume.

This ensures that:

- Dashboards remain available after container restarts
- Data source configuration is retained
- Dashboard customisations are preserved

---

## Accessing Grafana

When running with Docker Compose, Grafana is available at:

```text
http://localhost:3000
```

Default credentials:

```text
Username: admin
Password: admin
```

> Change the default password after the initial login when using Pulse outside of local development.

---

## Dashboard Screenshots

Example dashboard:

```text
screenshots/grafana-dashboard.png
```

The dashboard currently includes panels for:

- CPU Usage
- Memory Usage
- Disk Usage
- System Uptime

---

## Future Dashboard Enhancements

Future releases will expand the Grafana dashboard with additional operational insights.

Planned improvements include:

- Network traffic monitoring
- Container health panels
- Alert status overview
- Service availability indicators
- Historical trend analysis
- Dashboard variables and filtering
- Dark/light dashboard themes
- Multi-host monitoring
- Incident timeline visualisation

---

## Design Principles

The dashboard has been designed around several key principles.

### Simplicity

Present the most important infrastructure metrics without unnecessary complexity.

### Readability

Use clear visualisations that allow issues to be identified quickly.

### Operational Awareness

Provide an immediate overview of overall system health.

### Extensibility

Allow new metrics and dashboard panels to be added as Pulse continues to evolve.

---

## Related Documentation

- [Monitoring Stack](./monitoring-stack.md)
- [Architecture](./architecture.md)
- [Alerting](./alerting.md)
- [Configuration](./configuration.md)