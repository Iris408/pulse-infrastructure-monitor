![Backend CI](https://github.com/Iris408/system-health-monitor/actions/workflows/backend-ci.yml/badge.svg)

# System Health Monitor / システム健全性監視

A production-style Python monitoring project for tracking CPU, memory, disk usage, and uptime. It includes FastAPI health and metrics endpoints, threshold-based alerts, structured logging, Docker Compose, Prometheus, Grafana, and GitHub Actions CI/CD.

CPU、メモリ、ディスク使用量、稼働時間を監視する、本番環境を意識したPythonプロジェクトです。FastAPIのヘルス・メトリクスエンドポイント、しきい値アラート、構造化ログ、Docker Compose、Prometheus、Grafana、GitHub Actions CI/CDを含みます。

## Screenshots

### Terminal Monitor

<img src="./screenshots/system-health-monitor.png" width="300"/>

### Grafana Dashboard

<img src="./screenshots/grafana-dashboard.png" width="300"/>

## Current Status / 現在のステータス

The core monitoring and observability stack is complete. Future development will focus on testing, alerting improvements, deployment, and production configuration.

| Feature | Status |
| --- | --- |
| CPU, memory, disk, and uptime monitoring | ✅ Complete |
| Warning and critical threshold detection | ✅ Complete |
| Slack and email alerts | ✅ Complete |
| Alert cooldowns and recovery alerts | ✅ Complete |
| Structured logging | ✅ Complete |
| FastAPI `/health` endpoint | ✅ Complete |
| Docker container support | ✅ Complete |
| Docker healthcheck | ✅ Complete |
| Prometheus `/metrics` endpoint | ✅ Complete |
| Prometheus scrape configuration | ✅ Complete |
| Grafana service with persistent volume | ✅ Complete |
| Grafana dashboard panels | ✅ Complete |
| GitHub Actions CI/CD health endpoint check | ✅ Complete |
| EN/JP comments for learning and review | ✅ Complete |

## Features / 機能

- Terminal-based system monitoring
- CPU, memory, disk, and uptime checks
- Configurable warning and critical thresholds
- Slack and email alert support
- Cooldown logic to prevent repeated alerts
- Recovery alerts when metrics return to OK
- Structured logs in `logs/system_health.log`
- Readable health logs in `logs/health_log.txt`
- FastAPI `/health` endpoint
- Prometheus-compatible `/metrics` endpoint
- Prometheus scrape configuration with Docker Compose
- Grafana service connected to Prometheus
- Basic Grafana dashboard for CPU, memory, disk, and uptime
- Docker Compose support
- GitHub Actions CI/CD pipeline

## Health API

Run the FastAPI health API:

```bash
python3 -m uvicorn health_api:app --reload --port 8000
```

Check the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Local URLs:

| Page | URL |
| --- | --- |
| API Root | http://localhost:8000 |
| Health Endpoint | http://localhost:8000/health |
| Swagger UI | http://localhost:8000/docs |

## Docker Usage

Build and run:

```bash
docker compose up --build
```

Run in the background:

```bash
docker compose up -d
```

Check the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Stop the container:

```bash
docker compose down
```

## Monitoring Stack

The Docker Compose monitoring stack includes:

- FastAPI application with `/health` and `/metrics` endpoints
- Prometheus metric collection and scrape configuration
- Grafana connected to Prometheus
- Dashboard panels for CPU, memory, disk usage, and uptime
- Persistent Grafana storage

Detailed setup and configuration:

[Monitoring Stack Documentation](./docs/monitoring-stack.md)

## CI/CD

GitHub Actions validates the Python application and Docker deployment on every push and pull request.

## Installation

Clone the repository:

```bash
git clone https://github.com/Iris408/system-health-monitor.git
cd system-health-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the terminal monitor:

```bash
python3 main.py
```

Run the FastAPI health API:

```bash
python3 -m uvicorn health_api:app --reload --port 8000
```

## Project Structure

```text
system-health-monitor/
├── docs/
│   ├── monitoring-stack.md
│   └── project-details.md
├── screenshots/
│   ├── grafana-dashboard.png
│   ├── screenshot.png
│   └── system-health-monitor.png
├── examples/
│   ├── health_log.txt
├── alerts.py
├── dashboard.py
├── email_alerts.py
├── .env.example
├── health_api.py
├── logger.py
├── main.py
├── prometheus.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Tech Stack

- Python
- FastAPI
- psutil
- Prometheus
- Grafana
- Docker
- Docker Compose
- GitHub Actions
- colorama
- python-dotenv
- requests
- Slack Webhooks
- SMTP Email

## Additional Documentation

More detailed project documentation is available in the `docs/` folder.

| Document | Description |
| --- | --- |
| [Monitoring Stack](./docs/monitoring-stack.md) | Prometheus, Grafana, Docker Compose, and metrics setup |
| [Project Details](./docs/project-details.md) | Environment variables, logs, learning notes, and development notes |

## Author

Built by Iris408