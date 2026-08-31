# Logging

## Overview

Pulse uses structured logging to record monitoring activity, alert events, recovery events, and system status throughout the application's lifecycle.

Logging provides operational visibility, assists with troubleshooting, and creates a historical record of monitoring behaviour.

Rather than relying solely on terminal output, Pulse writes important events to dedicated log files that can be reviewed during development and troubleshooting.

---

## Logging Objectives

The Pulse logging system is designed to:

- Record important monitoring events
- Record alert and recovery behaviour
- Assist with debugging and troubleshooting
- Maintain an operational history
- Separate persistent monitoring information from terminal output
- Provide context when investigating monitoring or notification behaviour

---

## Logging Architecture

```text
System Metrics
       │
       ▼
Monitoring Engine
       │
       ▼
Structured Logging
       │
       ├──────────────► Terminal Output
       │
       └──────────────► Log Files
```

Logging operates alongside monitoring and alerting so that important application behaviour can be recorded independently of the visual monitoring interfaces.

Within the modular Pulse application structure, logging responsibilities are separated under:

```text
app/logging/
```

This keeps logging behaviour separate from metric collection, alert delivery, and API responsibilities.

---

## Log Files

Pulse currently uses two primary log files.

| File | Purpose |
| --- | --- |
| `logs/system_health.log` | Structured monitoring and alert event log |
| `logs/health_log.txt` | Human-readable health monitoring history |

Each file provides a different view of monitoring activity while remaining straightforward to inspect during development and troubleshooting.

---

## Structured Event Log

The structured system health log records operational events using consistent event information.

Examples include:

- Metric checks
- Alerts sent
- Alerts skipped because of cooldown behaviour
- Recovery notifications

Example entries:

```text
2026-07-12 12:40:10 | INFO | event=metric_check | metric=cpu | value=31.5 | status_level=OK
2026-07-12 12:40:10 | WARNING | event=alert_sent | metric=memory | value=82.1 | status_level=WARNING | channel=slack
2026-07-12 13:10:10 | INFO | event=alert_skipped | metric=memory | value=81.4 | status_level=WARNING | reason=cooldown
```

Using consistent fields makes monitoring behaviour easier to inspect than relying only on unstructured terminal messages.

---

## Logged Events

Current structured events include:

| Event | Meaning |
| --- | --- |
| `metric_check` | A monitored system metric was checked |
| `alert_sent` | An alert notification was generated and sent |
| `alert_skipped` | An alert was suppressed because cooldown behaviour was active |
| `recovery_alert_sent` | A monitored metric returned to a healthy state after an alert condition |

Depending on the event, additional information can include:

- Timestamp
- Metric name
- Measured value
- Status level
- Notification channel
- Cooldown reason

---

## Health Log

The health log provides a simpler human-readable history of monitoring activity.

It complements the structured event log by providing an easier way to review system health information without interpreting individual structured fields.

The two logs therefore serve different purposes:

```text
health_log.txt
     │
     └── Human-readable monitoring history

system_health.log
     │
     └── Structured operational events
```

---

## Logging During Monitoring

Monitoring activity can generate structured log entries containing information such as:

- Metric name
- Current metric value
- Current status
- Time of the monitoring event

This provides a record of how Pulse interpreted system resource usage during monitoring.

---

## Logging During Alerts

Alert behaviour is also recorded through the structured logging system.

Relevant events can include:

- Alert generated
- Notification channel
- Metric responsible for the alert
- Current metric value
- Warning or critical state
- Alert skipped because of cooldown behaviour
- Recovery notification

This creates an operational record that can be reviewed when investigating monitoring or notification behaviour.

---

## Cooldown Logging

Pulse records when an alert is suppressed because the configured cooldown period is still active.

Example:

```text
2026-07-12 13:10:10 | INFO | event=alert_skipped | metric=memory | value=81.4 | status_level=WARNING | reason=cooldown
```

Recording skipped alerts is useful because the absence of another notification does not necessarily mean that the monitored condition has recovered.

It may instead indicate that Pulse correctly suppressed a repeated notification.

---

## Recovery Logging

When a monitored metric returns to a healthy state after previously entering a warning or critical condition, Pulse can record the recovery event.

This allows the logs to show both sides of a monitoring event:

```text
Threshold exceeded
       │
       ▼
Alert generated
       │
       ▼
Cooldown / continued monitoring
       │
       ▼
Metric returns to healthy state
       │
       ▼
Recovery recorded
```

Recovery logging provides additional context when reviewing previous monitoring behaviour.

---

## Error and Failure Visibility

Operational failures should be visible through application logging where supported by the relevant component.

Examples of failures that may require investigation include:

- Slack notification failures
- SMTP connection problems
- Metric collection problems
- Configuration problems
- Unexpected application errors

Logging these failures helps distinguish between:

```text
Monitoring condition detected
```

and:

```text
Monitoring condition detected
but notification delivery failed
```

Improving failure visibility remains an area for maintenance where required.

---

## Relationship to Prometheus and Grafana

Pulse logs and Prometheus metrics serve different purposes.

### Logs

Logs record discrete operational events and application behaviour.

Examples include:

- Metric checks
- Alerts
- Cooldown decisions
- Recovery events

### Prometheus

Prometheus collects time-series metric data exposed by Pulse.

Examples include:

- CPU usage
- Memory usage
- Disk usage
- System uptime

### Grafana

Grafana queries Prometheus and provides visual monitoring dashboards.

Together, these provide complementary forms of observability:

```text
Pulse
  │
  ├────────► Structured Logs
  │
  └────────► /metrics
                │
                ▼
           Prometheus
                │
                ▼
             Grafana
```

Logs help explain application and alert behaviour, while Prometheus and Grafana provide metric-based monitoring and visualisation.

---

## Benefits of Logging

### Troubleshooting

Logs provide additional context when investigating unexpected monitoring or alerting behaviour.

### Operational History

Persisted logs provide a record of previous monitoring events that can be reviewed after they occur.

### Alert Visibility

Structured events make it possible to distinguish between alerts that were sent, alerts that were suppressed by cooldown behaviour, and recovery notifications.

### Development

During development and maintenance, logs provide another way to verify application behaviour without relying entirely on terminal output or Grafana dashboards.

---

## Security

Logs should not contain sensitive credentials or secrets.

Information that should not be written to logs includes:

- Slack webhook URLs
- SMTP passwords
- API keys
- Authentication credentials
- Environment secrets

Generated log files should not be committed to source control.

If sensitive information is accidentally logged or committed, the affected credentials should be rotated and the exposure investigated.

---

## Maintenance

The current logging implementation forms part of the completed Pulse monitoring platform.

Future logging work should focus on maintaining and improving the existing operational logging behaviour rather than expanding Pulse into a dedicated logging or incident-management platform.

Maintenance may include:

- Improved failure logging
- More consistent structured fields
- Configurable log levels
- Log rotation
- Logging tests
- Configuration improvements
- Dependency updates
- Documentation updates

Capabilities such as centralised log aggregation, incident IDs, incident timelines, database-backed alert history, and dedicated monitoring analytics are outside the current Pulse scope.

If a future engineering requirement justifies those capabilities, they can be evaluated separately rather than remaining part of the active maintenance backlog.

---

## Best Practices

When working with Pulse:

- Use logs alongside Prometheus and Grafana when troubleshooting.
- Do not commit generated log files to source control.
- Do not log passwords, webhook URLs, API keys, or other secrets.
- Review logging behaviour when changing monitoring or alert logic.
- Consider log retention and rotation when running the application for extended periods.
- Keep structured event names and fields consistent.

---

## Related Documentation

- [Alerting](./alerting.md)
- [Architecture](./architecture.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Project Details](./project-details.md)
- [Roadmap](./roadmap.md)
- [Troubleshooting](./troubleshooting.md)