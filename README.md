![Backend CI](https://github.com/Iris408/system-health-monitor/actions/workflows/backend-ci.yml/badge.svg)

# System Health Monitor / システム健全性監視

A Python system monitoring project that tracks CPU, memory, disk usage, and uptime. It includes threshold-based alerts, Slack/email notifications, alert cooldowns, recovery alerts, structured logging, a FastAPI `/health` endpoint, Docker healthchecks, and GitHub Actions CI/CD validation.

CPU、メモリ、ディスク使用量、稼働時間を監視する Python プロジェクトです。しきい値ベースのアラート、Slack/メール通知、アラートクールダウン、回復アラート、構造化ログ、FastAPI `/health` エンドポイント、Docker ヘルスチェック、GitHub Actions CI/CD 検証を含みます。

## Screenshot / スクリーンショット

<img src="./screenshots/system-health-monitor.png" width="500"/>

## Current Status / 現在のステータス

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

## CI/CD

GitHub Actions runs automated checks on push and pull request.

Current pipeline:

- Install Python dependencies
- Validate Python syntax
- Check key module imports
- Run tests when available
- Build Docker image
- Start Docker container
- Call the FastAPI `/health` endpoint
- Fail if the health endpoint does not respond

## Environment Variables

Create a `.env` file in the project root:

```env
SLACK_WEBHOOK_URL=your_slack_webhook_url
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient@example.com

OK_THRESHOLD=45
WARNING_THRESHOLD=75
CRITICAL_THRESHOLD=95
REFRESH_INTERVAL=300
ALERT_COOLDOWN_SECONDS=1800
```

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

## Logs

| Log File | Purpose |
| --- | --- |
| `logs/health_log.txt` | Readable health check history |
| `logs/system_health.log` | Structured event log for metrics, alerts, skipped alerts, and recovery events |

Example structured log:

```text
2026-07-12 12:40:10 | INFO | event=metric_check | metric=cpu | value=31.5 | status_level=OK
2026-07-12 12:40:10 | WARNING | event=alert_sent | metric=memory | value=82.1 | status_level=WARNING | channel=slack
2026-07-12 13:10:10 | INFO | event=alert_skipped | metric=memory | value=81.4 | status_level=WARNING | reason=cooldown
```

## Tech Stack

- Python
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- psutil
- colorama
- python-dotenv
- requests
- Slack Webhooks
- SMTP Email

## Next Roadmap

- Add `/metrics` endpoint for Prometheus
- Add alert history storage
- Add `/alerts` endpoint
- Add automated tests
- Add architecture diagram
- Add PostgreSQL or SQLite alert storage
- Add basic Grafana dashboard after Prometheus metrics are working

## What I Learned

Through this project, I practiced:

- Reading system metrics with Python
- Building a terminal-based monitoring tool
- Creating threshold-based alerts
- Sending Slack and email alerts
- Adding alert cooldown and recovery logic
- Writing structured logs
- Creating a FastAPI health endpoint
- Running the project with Docker Compose
- Validating the health endpoint through GitHub Actions CI/CD

## Author

Built by Iris408