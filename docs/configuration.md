# Configuration

## Overview

Pulse uses environment variables to configure monitoring behaviour, alerting, logging, and external integrations.

During local development, configuration is loaded from a `.env` file. A `.env.example` file is provided as a template for configuring a new installation.

Using environment variables keeps runtime configuration separate from the application source code and prevents sensitive credentials from being hardcoded.

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

The `.env` file should remain local and must not be committed to source control.

---

## Monitoring Configuration

The monitoring configuration controls how frequently Pulse collects system resource information.

| Variable | Description | Example |
| --- | --- | --- |
| `REFRESH_INTERVAL` | Monitoring interval in seconds | `5` |

Lower intervals provide more frequent monitoring updates but also increase how often system metrics are collected.

---

## CPU Thresholds

CPU thresholds determine when CPU usage should be treated as warning or critical.

| Variable | Description | Example |
| --- | --- | --- |
| `CPU_WARNING` | CPU usage warning threshold (%) | `80` |
| `CPU_CRITICAL` | CPU usage critical threshold (%) | `90` |

---

## Memory Thresholds

Memory thresholds determine when memory usage should be treated as warning or critical.

| Variable | Description | Example |
| --- | --- | --- |
| `MEMORY_WARNING` | Memory usage warning threshold (%) | `80` |
| `MEMORY_CRITICAL` | Memory usage critical threshold (%) | `90` |

---

## Disk Thresholds

Disk thresholds determine when disk usage should be treated as warning or critical.

| Variable | Description | Example |
| --- | --- | --- |
| `DISK_WARNING` | Disk usage warning threshold (%) | `85` |
| `DISK_CRITICAL` | Disk usage critical threshold (%) | `95` |

---

## Slack Configuration

Pulse supports Slack notifications through Incoming Webhooks.

| Variable | Description |
| --- | --- |
| `SLACK_WEBHOOK_URL` | Slack Incoming Webhook URL used for alert delivery |

When configured, Pulse can send monitoring alerts to the Slack channel associated with the webhook.

Webhook URLs should be treated as secrets and must not be committed to the repository.

---

## Email Configuration

Pulse supports email notifications through SMTP.

| Variable | Description |
| --- | --- |
| `SMTP_SERVER` | SMTP server hostname |
| `SMTP_PORT` | SMTP server port |
| `SMTP_USERNAME` | SMTP authentication username |
| `SMTP_PASSWORD` | SMTP authentication password or app password |
| `EMAIL_FROM` | Sender email address |
| `EMAIL_TO` | Recipient email address |

These values are required when email alerting is configured.

Email credentials should be stored in the local environment configuration rather than directly within the application source code.

---

## Docker Configuration

Pulse can run as part of a Docker Compose monitoring stack.

The stack includes:

- Pulse
- Prometheus
- Grafana

Container configuration and service relationships are defined in:

```text
docker-compose.yml
```

Docker Compose provides a repeatable environment for running the complete monitoring and observability stack.

---

## Prometheus Configuration

Prometheus is configured separately from the Python application.

The Prometheus configuration is stored under the project's configuration structure and defines how Prometheus discovers and scrapes Pulse.

Pulse exposes Prometheus-compatible metrics through:

```text
/metrics
```

Prometheus periodically scrapes this endpoint and stores the resulting time-series metric data.

See [Monitoring Stack](./monitoring-stack.md) for more information about the Prometheus integration.

---

## Grafana Configuration

Grafana uses Prometheus as its monitoring data source.

The current Pulse Grafana dashboard visualises:

- CPU usage
- Memory usage
- Disk usage
- System uptime

Grafana data is stored using persistent Docker storage so dashboard configuration can remain available between container restarts.

See [Grafana Dashboard](./grafana-dashboard.md) for dashboard-specific documentation.

---

## Logging Configuration

Pulse writes operational monitoring information to the `logs/` directory.

Current log files include:

```text
logs/
├── health_log.txt
└── system_health.log
```

These files provide monitoring history and structured operational information that can assist with troubleshooting and reviewing alert behaviour.

See [Logging](./logging.md) for additional information.

---

## Security

Sensitive configuration values must not be committed to source control.

Examples include:

- Slack webhook URLs
- SMTP passwords
- Email credentials
- API keys
- Authentication credentials

Use the following approach for local configuration:

1. Store sensitive values in `.env`.
2. Commit only `.env.example`.
3. Ensure `.env` is excluded through `.gitignore`.
4. Use placeholder values in documentation and examples.
5. Rotate credentials if they are accidentally exposed.

For hosted environments, secrets should be supplied through the environment or the platform's secret-management mechanism rather than committed configuration files.

---

## Example Development Configuration

The following values provide an example starting point for local development:

| Setting | Value |
| --- | ---: |
| Refresh Interval | 5 seconds |
| CPU Warning | 80% |
| CPU Critical | 90% |
| Memory Warning | 80% |
| Memory Critical | 90% |
| Disk Warning | 85% |
| Disk Critical | 95% |

These values are examples rather than universal infrastructure recommendations.

Monitoring thresholds should be selected according to the behaviour and requirements of the environment being monitored.

---

## Operational Considerations

When running Pulse outside a basic local development environment, consider:

- Supplying configuration through environment variables
- Managing secrets through the deployment environment
- Restricting access to sensitive configuration
- Protecting externally exposed services appropriately
- Reviewing log retention and rotation
- Keeping dependencies and container images updated
- Validating Docker configuration after infrastructure changes
- Reviewing alert behaviour after configuration changes

Pulse is currently intended as a single-environment monitoring project. Multi-host monitoring, incident-management infrastructure, and large-scale distributed monitoring are outside the current project scope.

---

## Maintenance

Configuration changes should remain focused on reliability and maintainability.

Potential maintenance work includes:

- Configuration validation
- Clearer handling of missing environment variables
- Improved secret handling
- Docker environment configuration
- Logging configuration improvements
- Automated configuration tests
- Documentation updates

Major configuration systems or infrastructure expansion are not required for the current Pulse feature scope.

---

## Related Documentation

- [Alerting](./alerting.md)
- [Architecture](./architecture.md)
- [Logging](./logging.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Roadmap](./roadmap.md)
- [Setup Guide](./setup.md)
- [Troubleshooting](./troubleshooting.md)