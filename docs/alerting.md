# Alerting

## Overview

Pulse includes a configurable alerting system designed to notify users when monitored system metrics exceed defined thresholds.

The alerting system complements the Prometheus and Grafana monitoring stack by providing direct notifications when system resource usage requires attention.

Pulse currently supports Slack and email notifications, alert cooldowns, recovery notifications, and structured logging of alert activity.

---

## Alert Workflow

The monitoring process follows a simple sequence.

```text
Collect System Metrics
          │
          ▼
Compare Against Thresholds
          │
          ▼
Threshold Exceeded?
      │           │
     No          Yes
      │           │
      ▼           ▼
 Continue     Generate Alert
                  │
                  ▼
          Send Notification
                  │
                  ▼
           Record in Logs
```

When a monitored metric returns to a healthy state after previously exceeding a threshold, Pulse can also generate a recovery notification.

---

## Supported Notification Channels

### Slack

Slack notifications are delivered using Incoming Webhooks.

Alert information can include:

- Metric name
- Current value
- Threshold status
- Time of detection

Slack provides a straightforward channel for receiving operational monitoring alerts.

---

### Email

Pulse also supports email notifications through SMTP.

Email alerts provide monitoring information when configured thresholds are exceeded and use the email settings provided through the application's environment configuration.

---

## Alert Thresholds

Pulse uses configurable thresholds to determine the health state of monitored system metrics.

The application supports:

- Normal / healthy status
- Warning status
- Critical status

Threshold values are controlled through application configuration rather than being fixed within the monitoring workflow.

Example threshold configuration:

```env
OK_THRESHOLD=45
WARNING_THRESHOLD=75
CRITICAL_THRESHOLD=95
```

The configured values determine when monitored resource usage should be treated as normal, warning, or critical.

See [Configuration](./configuration.md) for the current environment variable reference.

---

## Alert Cooldowns

Pulse implements cooldown logic to prevent repeated notifications for the same ongoing condition.

After an alert is sent, additional notifications for that condition can be temporarily suppressed until the configured cooldown period expires.

The cooldown duration is controlled through:

```env
ALERT_COOLDOWN_SECONDS=1800
```

This behaviour helps provide:

- Reduced notification noise
- More useful operational alerts
- Better readability during prolonged resource usage events
- Protection against repeatedly sending the same alert

---

## Recovery Alerts

Pulse can generate a recovery notification when a monitored metric returns to a healthy state after previously entering a warning or critical state.

For example:

```text
CPU usage has returned to normal levels.
Current value: 42%
Status: Healthy
```

Recovery notifications provide confirmation that the monitored condition has returned to an acceptable level without requiring the operator to continually inspect the monitoring dashboard.

---

## Structured Logging

Alert activity is recorded through Pulse's structured logging system.

Recorded events can include:

- Metric checks
- Alerts sent
- Alerts skipped because of cooldown behaviour
- Recovery notifications

Example:

```text
2026-07-12 12:40:10 | WARNING | event=alert_sent | metric=memory | value=82.1 | status_level=WARNING | channel=slack
2026-07-12 13:10:10 | INFO | event=alert_skipped | metric=memory | value=81.4 | status_level=WARNING | reason=cooldown
```

Structured alert logging provides an operational record that can be used when reviewing monitoring behaviour or troubleshooting notification issues.

See [Logging](./logging.md) for additional information about Pulse's logging architecture.

---

## Configuration

Alert behaviour is configured through environment variables.

Current alert-related configuration includes:

```env
SLACK_WEBHOOK_URL=your_slack_webhook_url
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient@example.com

OK_THRESHOLD=45
WARNING_THRESHOLD=75
CRITICAL_THRESHOLD=95
ALERT_COOLDOWN_SECONDS=1800
```

These settings control:

- Slack notification delivery
- Email notification delivery
- Monitoring thresholds
- Alert cooldown timing

Sensitive values such as webhook URLs and email credentials should not be committed to the repository.

See [Configuration](./configuration.md) for the complete configuration reference.

---

## Current Capabilities

The current Pulse alerting implementation supports:

- CPU alerts
- Memory alerts
- Disk alerts
- Warning and critical threshold behaviour
- Slack notifications
- Email notifications
- Configurable alert cooldowns
- Recovery notifications
- Structured alert logging

These capabilities form the completed alerting scope for the current Pulse monitoring platform.

---

## Maintenance

The current alerting feature cycle is complete.

Future work is focused on improving the reliability and maintainability of the existing alerting system rather than expanding it into a larger incident-management platform.

Maintenance work may include:

- More consistent alert formatting
- Improved alert metadata
- Alert failure handling
- Cooldown reliability improvements
- Recovery notification reliability
- Automated alert behaviour tests
- Configuration validation
- Operational logging improvements
- Dependency and security maintenance

Features such as additional notification providers, incident management, acknowledgement workflows, escalation policies, and persistent alert-history systems are outside the current Pulse scope.

If a future engineering requirement provides a clear reason for those capabilities, they can be evaluated separately rather than remaining on the active maintenance backlog.

---

## Design Principles

The alerting system follows four core principles.

### Reliability

Alerts should behave consistently when monitored resources cross configured thresholds.

### Simplicity

Notifications should provide the information required to understand the monitored condition without unnecessary complexity.

### Maintainability

Alerting components should remain separated from metric collection and API responsibilities so that existing behaviour can be tested and maintained independently.

### Operational Awareness

Alerting should communicate both unhealthy conditions and recovery, providing a clearer picture of changes in infrastructure health.

---

## Related Documentation

- [Configuration](./configuration.md)
- [Logging](./logging.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Architecture](./architecture.md)
- [Roadmap](./roadmap.md)