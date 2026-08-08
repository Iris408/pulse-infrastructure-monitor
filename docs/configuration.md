# Configuration

## Overview

Pulse uses environment variables to configure monitoring behaviour, alerting, logging, and external integrations.

Configuration is loaded from a local `.env` file during development. A `.env.example` file is provided as a template for new installations.

Environment variables allow the application to be configured without modifying the source code.

---

## Environment File

Create a `.env` file in the project root.

Example:

```env
REFRESH_INTERVAL=5

CPU_WARNING=80
CPU_CRITICAL=90

MEMORY_WARNING=80
MEMORY_CRITICAL=90

DISK_WARNING=85
DISK_CRITICAL=95

SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...

SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=example@example.com
SMTP_PASSWORD=your_password
EMAIL_FROM=example@example.com
EMAIL_TO=alerts@example.com
```

---

## Monitoring Configuration

These settings control how frequently Pulse collects system metrics.

| Variable | Description | Example |
|----------|-------------|---------|
| `REFRESH_INTERVAL` | Monitoring interval in seconds | `5` |

Lower values provide more responsive monitoring but increase CPU usage.

---

## CPU Thresholds

| Variable | Description | Example |
|----------|-------------|---------|
| `CPU_WARNING` | CPU usage warning threshold (%) | `80` |
| `CPU_CRITICAL` | CPU usage critical threshold (%) | `90` |

---

## Memory Thresholds

| Variable | Description | Example |
|----------|-------------|---------|
| `MEMORY_WARNING` | Memory usage warning threshold (%) | `80` |
| `MEMORY_CRITICAL` | Memory usage critical threshold (%) | `90` |

---

## Disk Thresholds

| Variable | Description | Example |
|----------|-------------|---------|
| `DISK_WARNING` | Disk usage warning threshold (%) | `85` |
| `DISK_CRITICAL` | Disk usage critical threshold (%) | `95` |

---

## Slack Configuration

Slack notifications use Incoming Webhooks.

| Variable | Description |
|----------|-------------|
| `SLACK_WEBHOOK_URL` | Slack Incoming Webhook URL |

When configured, Pulse sends monitoring alerts directly to the specified Slack channel.

---

## Email Configuration

Email alerts use an SMTP server.

| Variable | Description |
|----------|-------------|
| `SMTP_SERVER` | SMTP server hostname |
| `SMTP_PORT` | SMTP server port |
| `SMTP_USERNAME` | SMTP username |
| `SMTP_PASSWORD` | SMTP password |
| `EMAIL_FROM` | Sender email address |
| `EMAIL_TO` | Recipient email address |

These values are only required if email alerting is enabled.

---

## Docker Configuration

Pulse can be deployed using Docker Compose.

The default stack includes:

- Pulse Monitor
- Prometheus
- Grafana

Container-specific configuration is defined within `docker-compose.yml`.

---

## Prometheus Configuration

Prometheus is configured using:

```text
prometheus.yml
```

The default configuration scrapes the Pulse metrics endpoint.

```text
/metrics
```

---

## Grafana Configuration

Grafana connects to Prometheus as its primary data source.

Dashboard data is stored using a persistent Docker volume so dashboards remain available between container restarts.

---

## Logging Configuration

Pulse writes monitoring information to the `logs/` directory.

Current log files include:

- `system_health.log`
- `health_log.txt`

These files provide operational history and assist with troubleshooting.

---

## Security

Sensitive values should never be committed to source control.

Examples include:

- Slack webhook URLs
- SMTP passwords
- API keys
- Authentication credentials

Instead:

- Store secrets in `.env`
- Commit only `.env.example`
- Ensure `.env` is listed in `.gitignore`

---

## Recommended Development Configuration

The following values provide a good starting point for local development.

| Setting | Value |
|----------|------:|
| Refresh Interval | 5 seconds |
| CPU Warning | 80% |
| CPU Critical | 90% |
| Memory Warning | 80% |
| Memory Critical | 90% |
| Disk Warning | 85% |
| Disk Critical | 95% |

These values can be adjusted depending on the deployment environment.

---

## Production Considerations

For production deployments, consider:

- Using environment variables instead of hardcoded values
- Storing secrets in a secure secret manager
- Enabling log rotation
- Monitoring multiple hosts
- Configuring backup notification channels
- Using HTTPS for external integrations

---

## Related Documentation

- [Setup Guide](./setup.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Alerting](./alerting.md)
- [Troubleshooting](./troubleshooting.md)