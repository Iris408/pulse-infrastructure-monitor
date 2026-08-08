![Backend CI](https://github.com/Iris408/pulse-infrastructure-monitor/actions/workflows/backend-ci.yml/badge.svg)

# Pulse

**Infrastructure Health Monitoring Platform**

Pulse is a containerised infrastructure monitoring platform built with Python, FastAPI, Prometheus, and Grafana. It monitors system health, exposes operational metrics, provides Grafana dashboards, and supports configurable Slack and email alerting.

## Key Features

- CPU, memory, disk, and uptime monitoring
- Configurable warning and critical thresholds
- FastAPI `/health` and `/metrics` endpoints
- Prometheus metric collection
- Grafana infrastructure dashboard
- Slack and email notifications
- Alert cooldowns and recovery notifications
- Structured application logging
- Docker and Docker Compose deployment
- GitHub Actions CI

## Technology Stack

| Area | Technologies |
| --- | --- |
| Backend | Python, FastAPI, psutil |
| Observability | Prometheus, Grafana |
| Alerting | Slack Webhooks, SMTP Email |
| Infrastructure | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Configuration | python-dotenv |
| Utilities | requests, colorama |

## Architecture

```text
System Resources
       │
       ▼
  Pulse Monitor
       │
       ├──────────► Logging
       │
       ├──────────► Slack / Email Alerts
       │
       ▼
   FastAPI
 /health  /metrics
             │
             ▼
        Prometheus
             │
             ▼
          Grafana
```

For a more in-depth breakdown of the system design, please see the [Architecture Documentation](./docs/architecture.md).

## Screenshots

### Terminal Monitor

<img src="./screenshots/system-health-monitor.png" width="500" alt="Pulse terminal system monitor">

### Grafana Dashboard

<img src="./screenshots/grafana-dashboard.png" width="700" alt="Pulse Grafana infrastructure dashboard">

## Quick Start

### Local

Clone the repository:

```bash
git clone https://github.com/Iris408/pulse-infrastructure-monitor.git
cd pulse-infrastructure-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment configuration:

```bash
cp .env.example .env
```

Run the terminal monitor:

```bash
python3 main.py
```

Or start the FastAPI service:

```bash
python3 -m uvicorn health_api:app --reload --port 8000
```

### Docker

Start the complete monitoring stack:

```bash
docker compose up --build -d
```

Check service status:

```bash
docker compose ps
```

Stop the stack:

```bash
docker compose down
```

For more detailed installation and configuration instructions, please see the [Setup Guide](./docs/setup.md).

## Monitoring Endpoints

When running locally:

| Service | URL |
| --- | --- |
| API Root | `http://localhost:8000/` |
| Health | `http://localhost:8000/health` |
| Metrics | `http://localhost:8000/metrics` |
| Swagger UI | `http://localhost:8000/docs` |
| Prometheus | `http://localhost:9090` |
| Grafana | `http://localhost:3000` |

## Monitoring Stack

Pulse uses a containerised observability stack:

```text
Pulse
  │
  │ /metrics
  ▼
Prometheus
  │
  ▼
Grafana
```

Prometheus periodically checks metrics exposed by Pulse, while Grafana queries Prometheus to provide visual monitoring of CPU, memory, disk usage, and system uptime.

## Current Status

**Current release: v2.3.1**

The core monitoring and observability stack is complete.

| Capability | Status |
| --- | :---: |
| System resource monitoring | ✅ |
| Warning and critical thresholds | ✅ |
| Slack and email alerting | ✅ |
| Cooldowns and recovery alerts | ✅ |
| Structured logging | ✅ |
| FastAPI health API | ✅ |
| Prometheus metrics | ✅ |
| Grafana dashboards | ✅ |
| Docker Compose stack | ✅ |
| GitHub Actions CI | ✅ |

The next development phase will focus on alerting improvements, followed by automated testing and production configuration.

## Testing and CI

GitHub Actions automatically validates the application on pushes and pull requests to `main`.

The CI workflow provides automated checks for the Python application and Docker-based monitoring environment.

Additional automated testing is planned as part of the next development phases.

## Project Structure

```text
pulse-infrastructure-monitor/
├── docs/
├── screenshots/
├── examples/
├── alerts.py
├── dashboard.py
├── email_alerts.py
├── health_api.py
├── logger.py
├── main.py
├── prometheus.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

## Documentation

Detailed engineering documentation is available in [`docs/`](./docs/).

| Document | Description |
| --- | --- |
| [Architecture](./docs/architecture.md) | System architecture and component responsibilities |
| [Alerting](./docs/alerting.md) | Slack, email, thresholds, cooldowns, and recovery alerts |
| [Configuration](./docs/configuration.md) | Environment variables and application configuration |
| [Grafana Dashboard](./docs/grafana-dashboard.md) | Dashboard setup, metrics, and panels |
| [Logging](./docs/logging.md) | Logging architecture and operational logs |
| [Monitoring Stack](./docs/monitoring-stack.md) | FastAPI, Prometheus, Grafana, and Docker integration |
| [Setup](./docs/setup.md) | Local and Docker installation |
| [Troubleshooting](./docs/troubleshooting.md) | Common problems and diagnostic steps |
| [Roadmap](./docs/roadmap.md) | Current release and future development |
| [Learning Notes](./docs/learning-notes.md) | Technical lessons and engineering decisions |
| [Project Details](./docs/project-details.md) | Additional implementation details |

## Roadmap

### Current

**v2.3.1 — Grafana Dashboard** ✅

### Next

**v2.3.2 — Alerting Improvements**

Planned areas include structured alerts, improved severity handling, alert metadata, and incident identification.

Future development will introduce automated testing, production configuration improvements, and expanded monitoring capabilities.

See the full [Pulse Roadmap](./docs/roadmap.md).

## Author

Built by [Iris408](https://github.com/Iris408)