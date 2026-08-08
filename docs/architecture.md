# Pulse Architecture

## Overview

Pulse is a containerised infrastructure health monitoring platform built with Python, FastAPI, Prometheus, and Grafana.

The platform continuously monitors system resources, exposes health and metrics endpoints, provides operational dashboards, and supports alerting through Slack and email.

The architecture is intentionally modular, allowing monitoring, logging, alerting, metrics collection, and visualisation to evolve independently while remaining easy to understand and maintain.

---

## Architecture Goals

Pulse has been designed around the following principles:

- Separation of responsibilities
- Modular services
- Production-style project structure
- Containerised deployment
- Extensible monitoring and alerting
- Simple deployment using Docker Compose

---

## High-Level Architecture

```text
                    ┌──────────────────────┐
                    │    System Resources  │
                    │ CPU • Memory • Disk  │
                    │ Uptime • Processes   │
                    └──────────┬───────────┘
                               │
                               ▼
                      ┌─────────────────┐
                      │   Pulse Monitor │
                      │    (main.py)    │
                      └────────┬────────┘
                               │
        ┌──────────────┬───────────────┬──────────────┐
        ▼              ▼               ▼              ▼
   logger.py      alerts.py      dashboard.py   health_api.py
        │              │                              │
        │              │                              ▼
        │              │                      FastAPI Endpoints
        │              │                    /health • /metrics
        │              │                              │
        ▼              ▼                              ▼
   Log Files     Slack / Email                 Prometheus
                                                  │
                                                  ▼
                                              Grafana
```

---

## Component Responsibilities

### main.py

The main monitoring service.

Responsibilities include:

- Collecting system metrics
- Evaluating warning and critical thresholds
- Coordinating logging
- Triggering alerts
- Updating the monitoring dashboard

This acts as the orchestration layer for the application.

---

### health_api.py

Provides HTTP endpoints for external monitoring tools.

Current endpoints include:

- `/`
- `/health`
- `/metrics`

These endpoints allow Docker, Prometheus, and external services to verify application health and collect metrics.

---

### logger.py

Responsible for structured logging.

Logs operational information including:

- System health
- Alerts
- Threshold events
- Monitoring activity

Logs are written to the project's log files for later review.

---

### alerts.py

Handles notification delivery.

Current integrations include:

- Slack
- Email

Alert cooldown logic prevents duplicate notifications during sustained incidents.

---

### dashboard.py

Displays the local terminal monitoring dashboard.

Provides a real-time view of:

- CPU usage
- Memory usage
- Disk usage
- Uptime
- Overall application status

---

## Monitoring Flow

The monitoring process follows a simple continuous workflow.

```text
Collect Metrics
        │
        ▼
Evaluate Thresholds
        │
        ▼
Generate Alerts
        │
        ▼
Write Logs
        │
        ▼
Expose Metrics
        │
        ▼
Visualise in Grafana
```

---

## Docker Architecture

Pulse is deployed using Docker Compose.

The monitoring stack consists of three primary services.

| Service | Purpose |
|----------|---------|
| Pulse Monitor | Collects metrics and exposes APIs |
| Prometheus | Scrapes and stores metrics |
| Grafana | Visualises operational dashboards |

---

## Technology Stack

### Backend

- Python
- FastAPI

### Monitoring

- psutil
- Prometheus
- Grafana

### Infrastructure

- Docker
- Docker Compose
- GitHub Actions

### Notifications

- Slack Webhooks
- SMTP Email

---

## Design Principles

Pulse follows several engineering principles throughout the project.

### Separation of Concerns

Each module has a single responsibility.

Examples include monitoring, logging, alerting, and API endpoints.

---

### Extensibility

New monitoring capabilities can be added without major architectural changes.

Examples include:

- Additional system metrics
- New alert providers
- Database-backed alert history
- Incident management

---

### Maintainability

The project favours readable code, modular components, and concise documentation to simplify future development.

---

## Future Architecture

Future versions will expand the architecture with:

- Structured alert models
- Incident IDs
- Alert history
- Multiple notification providers
- Deployment configuration improvements
- Additional monitoring targets
- Expanded automated testing

These enhancements will build upon the existing modular architecture without requiring significant redesign.