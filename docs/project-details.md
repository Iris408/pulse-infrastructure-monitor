# Project Details

This document contains extra setup, logging, environment, and learning notes for the Infrastructure Health Monitoring Platform.

---

## Environment Variables

This project uses environment variables for alerting, threshold configuration, alert cooldowns, and automated refresh timing.

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

### Environment Variable Reference

| Variable | Purpose |
| --- | --- |
| `SLACK_WEBHOOK_URL` | Slack webhook used for alert notifications |
| `EMAIL_ADDRESS` | Sender email address |
| `EMAIL_PASSWORD` | Sender email password or app password |
| `TO_EMAIL` | Alert recipient email address |
| `OK_THRESHOLD` | Usage level considered normal |
| `WARNING_THRESHOLD` | Usage level that triggers warning status |
| `CRITICAL_THRESHOLD` | Usage level that triggers critical status |
| `REFRESH_INTERVAL` | Time between terminal monitor checks |
| `ALERT_COOLDOWN_SECONDS` | Cooldown time before repeating similar alerts |

---

## Logs

The project writes two types of logs.

| Log File | Purpose |
| --- | --- |
| `logs/health_log.txt` | Readable health check history |
| `logs/system_health.log` | Structured event log for metrics, alerts, skipped alerts, and recovery events |

### Example Structured Logs

```text
2026-07-12 12:40:10 | INFO | event=metric_check | metric=cpu | value=31.5 | status_level=OK
2026-07-12 12:40:10 | WARNING | event=alert_sent | metric=memory | value=82.1 | status_level=WARNING | channel=slack
2026-07-12 13:10:10 | INFO | event=alert_skipped | metric=memory | value=81.4 | status_level=WARNING | reason=cooldown
```

### Log Events

| Event | Meaning |
| --- | --- |
| `metric_check` | CPU, memory, or disk value was checked |
| `alert_sent` | Alert was sent through log, Slack, or email |
| `alert_skipped` | Alert was skipped because cooldown was active |
| `recovery_alert_sent` | Metric returned to OK after warning or critical state |

---

## What I Learned

Through this project, I practiced:

- Reading system metrics with Python
- Building a terminal-based monitoring tool
- Creating threshold-based alerts
- Sending Slack and email alerts
- Adding alert cooldown and recovery logic
- Writing structured logs
- Creating a FastAPI `/health` endpoint
- Creating a Prometheus-compatible `/metrics` endpoint
- Running the project with Docker Compose
- Adding Docker healthchecks
- Connecting Prometheus to a FastAPI metrics endpoint
- Connecting Grafana to Prometheus
- Creating basic Grafana dashboard panels
- Validating the health endpoint through GitHub Actions CI/CD

---

## Development Notes

This project started as a beginner Python monitoring script and has been expanded into a production-style monitoring platform.

Current production-style additions include:

- Structured logging
- Configurable alert cooldowns
- Recovery alerts
- FastAPI health API
- Prometheus metrics
- Docker Compose monitoring stack
- Grafana dashboard
- CI/CD health endpoint validation