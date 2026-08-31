# Pulse Architecture

## Overview

Pulse is a containerised infrastructure health monitoring and observability platform built with Python, FastAPI, Prometheus, and Grafana.

The platform monitors system resources, exposes health and Prometheus-compatible metrics endpoints, provides operational dashboards, and supports alerting through Slack and email.

Pulse uses a modular application structure that separates API, monitoring, alerting, logging, and dashboard responsibilities. This keeps the system easier to understand, test, and maintain as the project moves into maintenance.

---

## Architecture Goals

Pulse is designed around the following principles:

- Separation of concerns
- Modular application components
- Clear component responsibilities
- Containerised infrastructure
- Observable application behaviour
- Maintainable monitoring and alerting
- Simple local deployment with Docker Compose

---

## High-Level Architecture

```text
                    ┌──────────────────────┐
                    │   System Resources   │
                    │ CPU • Memory • Disk  │
                    │       Uptime         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Pulse Monitoring  │
                    │   app/monitoring/   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       app/logging/      app/alerts/       app/api/
              │                │                │
              ▼                ▼                ▼
        Structured       Slack / Email      FastAPI
           Logs                            /health
                                           /metrics
                                              │
                                              │ scrape
                                              ▼
                                         Prometheus
                                              │
                                              │ query
                                              ▼
                                           Grafana
```

The monitoring layer collects system resource information and coordinates the operational behaviour of Pulse.

Logging and alerting handle monitoring events and notifications, while the FastAPI layer exposes application health and metrics for external monitoring.

Prometheus scrapes the metrics endpoint and stores time-series metric data. Grafana queries Prometheus to provide visual infrastructure dashboards.

---

## Application Structure

The v2.3.2 refactor introduced a modular Python application structure.

```text
app/
├── api/
├── monitoring/
├── alerts/
├── logging/
└── dashboard/
```

Each package is responsible for a specific part of the monitoring platform.

---

## Component Responsibilities

### `app/api/`

Provides the HTTP interface for Pulse.

Current API functionality includes:

- Application root endpoint
- Health endpoint
- Prometheus-compatible metrics endpoint

Important endpoints include:

```text
/
/health
/metrics
```

The API allows external systems such as Docker and Prometheus to inspect application health and collect operational metrics.

---

### `app/monitoring/`

Contains the core system-monitoring behaviour.

Responsibilities include:

- Collecting CPU usage
- Collecting memory usage
- Collecting disk usage
- Tracking system uptime
- Evaluating configured thresholds
- Coordinating monitoring behaviour

This package represents the core monitoring domain of Pulse.

---

### `app/alerts/`

Contains notification and alert behaviour.

Current responsibilities include:

- Slack notifications
- Email notifications
- Warning and critical alert behaviour
- Alert cooldown handling
- Recovery notifications

Keeping notification behaviour separate from metric collection makes the alerting system easier to maintain and test independently.

---

### `app/logging/`

Handles operational and structured logging.

Logged activity can include:

- Metric checks
- Threshold events
- Alerts sent
- Alerts skipped because of cooldown behaviour
- Recovery events

Structured logging provides an operational history that can be used when reviewing monitoring behaviour or troubleshooting problems.

---

### `app/dashboard/`

Contains dashboard-related application components.

Pulse provides local monitoring output alongside its Grafana visualisation layer.

The dashboard components support visibility into:

- CPU usage
- Memory usage
- Disk usage
- System uptime
- Overall monitoring status

Grafana remains the primary visual observability interface for Prometheus metric data.

---

## Monitoring Flow

The core monitoring workflow can be represented as:

```text
Collect System Metrics
        │
        ▼
Evaluate Thresholds
        │
        ├──────────────► Write Structured Logs
        │
        ├──────────────► Trigger Alerts
        │
        ▼
Expose Metrics
        │
        ▼
Prometheus Scraping
        │
        ▼
Grafana Visualisation
```

This separates system monitoring from the external observability layer while allowing both to work from the same application behaviour.

---

## Observability Flow

Pulse exposes Prometheus-compatible metrics through FastAPI.

```text
Pulse
  │
  │ /metrics
  ▼
Prometheus
  │
  │ PromQL queries
  ▼
Grafana
```

Prometheus periodically scrapes the Pulse metrics endpoint.

Grafana uses Prometheus as its data source and provides dashboard panels for:

- CPU usage
- Memory usage
- Disk usage
- System uptime

This provides a separate observability layer from the terminal monitoring interface.

---

## Alerting Flow

Alerting operates alongside the monitoring workflow.

```text
System Metric
     │
     ▼
Threshold Evaluation
     │
     ├── Healthy ─────────► Continue Monitoring
     │
     ├── Warning ─────────► Alert Logic
     │
     └── Critical ────────► Alert Logic
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
                   Slack               Email
                     │                   │
                     └─────────┬─────────┘
                               ▼
                       Structured Logging
```

Cooldown behaviour helps prevent repeated notifications during sustained conditions.

Recovery notifications can be generated when a monitored metric returns to a healthy state.

---

## Docker Architecture

Pulse uses Docker Compose to run the monitoring and observability stack.

The primary services are:

| Service | Purpose |
| --- | --- |
| Pulse | Runs the monitoring application and FastAPI interface |
| Prometheus | Scrapes and stores operational metrics |
| Grafana | Queries Prometheus and visualises monitoring data |

The service relationship is:

```text
┌─────────────────┐
│      Pulse      │
│    FastAPI      │
│     :8000       │
└────────┬────────┘
         │
         │ scrape /metrics
         ▼
┌─────────────────┐
│   Prometheus    │
│      :9090      │
└────────┬────────┘
         │
         │ query
         ▼
┌─────────────────┐
│     Grafana     │
│      :3000      │
└─────────────────┘
```

Docker Compose provides a repeatable way to run the complete monitoring stack locally.

---

## Technology Stack

### Backend

- Python
- FastAPI
- psutil

### Observability

- Prometheus
- Grafana

### Alerting

- Slack Incoming Webhooks
- SMTP Email

### Infrastructure

- Docker
- Docker Compose

### CI

- GitHub Actions

### Configuration

- Environment variables
- python-dotenv

---

## Design Principles

### Separation of Concerns

Monitoring, API, alerting, logging, and dashboard responsibilities are separated into dedicated application packages.

This reduces coupling and makes individual parts of the system easier to understand and maintain.

### Observability

Pulse exposes operational information through multiple layers:

- Structured logs
- Health endpoint
- Prometheus metrics
- Grafana dashboards
- Slack and email notifications

Together, these provide visibility into both the monitored system and Pulse's monitoring behaviour.

### Maintainability

The project favours modular components, explicit configuration, containerised infrastructure, and focused documentation.

The v2.3.2 architecture refactor established the current structure for long-term maintenance.

### Reliability

Monitoring and alerting behaviour should remain predictable and testable.

Future maintenance therefore prioritises regression testing, alert reliability, configuration validation, and infrastructure checks over adding additional platform features.

---

## Maintenance Architecture

The current architecture represents the completed feature scope for Pulse.

Future architectural work should primarily support:

- Automated testing
- Alert reliability
- Dependency and security maintenance
- Configuration validation
- Docker and CI validation
- Logging improvements
- Bug fixes
- Documentation maintenance

Large architectural expansions such as multi-host monitoring, incident management, persistent alert-history platforms, or additional notification ecosystems are outside the current Pulse scope.

If a future engineering requirement justifies one of these capabilities, it should be evaluated as a separate major release rather than being treated as unfinished work in the current architecture.

---

## Related Documentation

- [Alerting](./alerting.md)
- [Configuration](./configuration.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Logging](./logging.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Project Details](./project-details.md)
- [Roadmap](./roadmap.md)
- [Setup](./setup.md)
- [Troubleshooting](./troubleshooting.md)