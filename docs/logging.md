# Logging

## Overview

Pulse uses structured logging to record monitoring activity, alert events, and system status throughout the application's lifecycle.

Logging provides operational visibility, assists with troubleshooting, and creates a historical record of system behaviour.

Rather than relying solely on terminal output, Pulse writes important events to dedicated log files that can be reviewed later.

---

## Logging Objectives

The logging system has been designed to:

- Record important monitoring events
- Assist with debugging and troubleshooting
- Maintain an operational history
- Support future alert auditing
- Separate monitoring information from application output

---

# Logging Architecture

```text
System Metrics
       │
       ▼
 Monitoring Engine
       │
       ▼
 Logger
       │
       ├──────────────► Terminal Output
       │
       └──────────────► Log Files
```

Every monitoring cycle can generate log entries depending on the current system state.

---

# Log Files

Pulse currently generates two primary log files.

| File | Purpose |
|------|---------|
| `logs/system_health.log` | Structured monitoring and alert log |
| `logs/health_log.txt` | Human-readable health history |

Each file serves a different purpose while remaining easy to inspect during development.

---

# Logged Events

The logging system records a variety of operational events.

Examples include:

- Application startup
- Monitoring cycles
- CPU threshold exceeded
- Memory threshold exceeded
- Disk threshold exceeded
- Alert delivery
- Recovery notifications
- Unexpected errors

---

# Structured Logging

Pulse records structured information wherever possible to improve readability and future extensibility.

Typical information includes:

- Timestamp
- Metric name
- Measured value
- Threshold
- Alert type
- Status

Example:

```text
2026-08-04 14:35:42

CPU Usage: 92%
Threshold: 90%
Status: Critical
```

Structured logging makes it easier to identify operational events without manually searching through unformatted console output.

---

# Health Log

The health log provides a simplified history of monitoring activity.

Typical entries include:

- Healthy
- Warning
- Critical
- Recovery

This log is intended to provide a quick overview of infrastructure health over time.

---

# Error Logging

Unexpected exceptions are also recorded.

Examples include:

- Notification failures
- SMTP connection issues
- Slack webhook failures
- Metric collection errors

Capturing these events helps diagnose operational problems while keeping the monitoring service running whenever possible.

---

# Logging During Alerts

Whenever an alert is generated, Pulse records the event before attempting notification delivery.

Typical alert logging includes:

- Alert type
- Current metric value
- Threshold exceeded
- Delivery status

This creates an audit trail for monitoring activity.

---

# Benefits of Logging

Maintaining detailed logs provides several advantages.

### Troubleshooting

Logs allow developers to identify the cause of unexpected behaviour after an incident has occurred.

---

### Operational History

Historical logs provide visibility into long-term system behaviour and recurring infrastructure issues.

---

### Development

During development, log files make it easier to verify monitoring logic without relying entirely on dashboard output.

---

### Future Incident Management

Structured logs provide the foundation for future features such as:

- Alert history
- Incident timelines
- Audit reports
- Monitoring analytics

---

# Future Improvements

Future versions of Pulse may introduce additional logging capabilities.

Planned improvements include:

- JSON structured logs
- Log rotation
- Configurable log levels
- Daily log files
- Centralised logging
- Correlation IDs
- Incident IDs
- Exportable log reports

---

# Best Practices

When working with Pulse:

- Review logs regularly during development.
- Do not commit generated log files to source control.
- Rotate logs in production environments.
- Avoid logging sensitive information such as passwords or API keys.
- Use logs alongside Grafana dashboards for a complete view of system behaviour.

---

# Related Documentation

- [Architecture](./architecture.md)
- [Alerting](./alerting.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Troubleshooting](./troubleshooting.md)