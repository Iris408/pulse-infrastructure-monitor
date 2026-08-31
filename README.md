![Backend CI](https://github.com/Iris408/pulse-infrastructure-monitor/actions/workflows/backend-ci.yml/badge.svg)

# 💓 Pulse

### Infrastructure Health Monitoring Platform

Pulse is a containerised infrastructure monitoring platform built with Python, FastAPI, Prometheus, and Grafana. It monitors system health, exposes operational metrics, provides Grafana dashboards, and supports configurable Slack and email alerting.

## Key Features

- CPU, memory, disk, and uptime monitoring
- Configurable warning and critical thresholds
- FastAPI `/health` and `/metrics` endpoints
- Prometheus-compatible metrics
- Grafana infrastructure dashboard
- Slack and email notifications
- Alert cooldowns and recovery notifications
- Structured application logging
- Containerised deployment with Docker Compose
- GitHub Actions backend CI

## Current Status

**Current release: v2.3.2** ✅  
**Lifecycle: Maintenance**

The core Pulse monitoring and observability stack is complete and portfolio-ready.

Pulse provides system resource monitoring, configurable Slack and email alerting, FastAPI health and metrics endpoints, Prometheus metric collection, Grafana visualisation, structured logging, Docker Compose deployment, and GitHub Actions CI.

v2.3.2 introduced a modular application structure separating the API, monitoring, alerting, logging, and dashboard components to improve maintainability.

Future work is limited to maintenance, automated testing, dependency and security updates, alert reliability, documentation, and infrastructure improvements.

See the [Roadmap](./docs/roadmap.md) for release history and maintenance work.

## Technology Stack

| Area | Technologies |
| --- | --- |
| Backend | Python, FastAPI, psutil |
| Observability | Prometheus, Grafana |
| Alerting | Slack Webhooks, SMTP Email |
| Infrastructure | Docker, Docker Compose |
| CI | GitHub Actions (Backend CI) |
| Configuration | python-dotenv |
| Utilities | requests, colorama |

## Architecture

```text
System Resources
       │
       ▼
  Pulse Monitor
       │
       ├──────────► Structured Logging
       │
       ├──────────► Slack / Email Alerts
       │
       ▼
    FastAPI
 /health  /metrics
       ▲
       │ scrapes
       │
   Prometheus
       │
       │ queries
       ▼
    Grafana
```

Prometheus periodically scrapes metrics exposed by Pulse, while Grafana queries Prometheus to provide visual monitoring of CPU, memory, disk usage, and system uptime.

For a more in-depth breakdown of the system design, please see the [Architecture Documentation](./docs/architecture.md).

## Screenshots

### Terminal Monitor

<img src="./screenshots/system-health-monitor.png" width="600" alt="Pulse terminal system monitor">

### Grafana Dashboard

<img src="./screenshots/grafana-dashboard.png" width="600" alt="Pulse Grafana infrastructure dashboard">

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

Create the environment configuration:

```bash
cp .env.example .env
```

Run the terminal monitor:

```bash
python3 main.py
```
**Or start the FastAPI service:**

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

## Testing and CI

GitHub Actions automatically validates the Python backend on pushes and pull requests to `main`.

The current CI workflow runs automated backend checks to help catch regressions before changes are merged.

Additional automated testing, security checks, and Docker validation are tracked as maintenance improvements.

## Project Structure

```text
pulse-infrastructure-monitor/
├── app/
│   ├── api/
│   ├── monitoring/
│   ├── alerts/
│   ├── logging/
│   └── dashboard/
├── tests/
├── config/
├── docs/
├── screenshots/
├── examples/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Documentation

Detailed engineering documentation is available in [`docs/`](./docs/).

| Document | Description |
| --- | --- |
| [Alerting](./docs/alerting.md) | Slack, email, thresholds, cooldowns, and recovery alerts |
| [Architecture](./docs/architecture.md) | System architecture and component responsibilities |
| [Configuration](./docs/configuration.md) | Environment variables and application configuration |
| [Grafana Dashboard](./docs/grafana-dashboard.md) | Dashboard setup, metrics, and panels |
| [Learning Notes](./docs/learning-notes.md) | Technical lessons and engineering decisions |
| [Logging](./docs/logging.md) | Logging architecture and operational logs |
| [Monitoring Stack](./docs/monitoring-stack.md) | FastAPI, Prometheus, Grafana, and Docker integration |
| [Project Details](./docs/project-details.md) | Additional implementation details |
| [Roadmap](./docs/roadmap.md) | Current release and future development |
| [Setup](./docs/setup.md) | Local and Docker installation |
| [Troubleshooting](./docs/troubleshooting.md) | Common problems and diagnostic steps |


## License
This project is licensed under the terms in [MIT LICENSE](./LICENSE) file for details.

## Author

Built by [Iris408](https://github.com/Iris408)