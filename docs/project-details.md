# Project Details

This document contains additional configuration, logging, engineering, and maintenance notes for Pulse.

---

## Environment Variables

Pulse uses environment variables for alerting, monitoring thresholds, alert cooldowns, and refresh timing.

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

Pulse writes two types of operational logs.

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

## Engineering Scope

Pulse began as a lightweight Python system-monitoring script and was incrementally developed into a production-style infrastructure monitoring and observability platform.

The completed platform includes:

- CPU, memory, disk, and uptime monitoring
- Configurable monitoring thresholds
- Slack and email alerting
- Alert cooldowns and recovery notifications
- Structured operational logging
- FastAPI health and metrics endpoints
- Prometheus metric collection
- Grafana visualisation
- Docker Compose infrastructure
- Container healthchecks
- GitHub Actions backend CI
- Modular application architecture

The current feature cycle is complete. Future engineering work is limited primarily to maintenance, testing, security, dependency updates, reliability improvements, and documentation.

---

## What I Learned

Through Pulse, I practised:

- Reading and interpreting system metrics with Python
- Building a terminal-based monitoring tool
- Designing threshold-based monitoring behaviour
- Sending Slack and email alerts
- Implementing alert cooldown and recovery logic
- Writing structured operational logs
- Building FastAPI health and metrics endpoints
- Exposing Prometheus-compatible metrics
- Running a multi-service monitoring stack with Docker Compose
- Adding Docker healthchecks
- Connecting Prometheus to a FastAPI metrics endpoint
- Connecting Grafana to Prometheus
- Building Grafana infrastructure dashboard panels
- Structuring a Python application into maintainable modules
- Validating backend behaviour through GitHub Actions CI

---

## Maintenance

Pulse is now maintained as a completed monitoring project rather than an actively expanding feature project.

Maintenance work may include:

- Automated test coverage
- Alert reliability improvements
- Dependency and security updates
- CI workflow improvements
- Docker validation
- Configuration improvements
- Documentation updates
- Bug fixes and small operational improvements

Large feature additions are outside the current project scope.

See the [Roadmap](./roadmap.md) for the maintenance plan.