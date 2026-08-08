# Alerting

## Overview

Pulse includes a configurable alerting system designed to notify users when monitored system metrics exceed defined thresholds.

Alerts help identify potential infrastructure issues before they become critical failures, allowing users and administrators to respond quickly and minimise downtime.

The alerting system currently supports Slack and email notifications, with additional providers planned for future releases.

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

---

## Supported Notification Channels

### Slack

Slack notifications are delivered using Incoming Webhooks.

Typical alert information includes:

- Metric name
- Current value
- Threshold exceeded
- Time of detection

Slack provides a simple method for receiving operational alerts in real time.

---

### Email

Pulse also supports SMTP email notifications.

Email alerts provide the same monitoring information and can be sent to one or more recipients depending on the configured SMTP settings.

---

## Alert Thresholds

Each monitored metric can define warning and critical limits.

Typical examples include:

| Metric | Warning | Critical |
|----------|---------|----------|
| CPU Usage | 80% | 90% |
| Memory Usage | 80% | 90% |
| Disk Usage | 85% | 95% |

Threshold values can be adjusted through the application's configuration.

---

## Alert Cooldowns

To avoid sending multiple identical notifications during a prolonged incident, Pulse implements cooldown logic.

This means that once an alert has been sent, additional notifications for the same condition are temporarily suppressed until the cooldown period expires.

Benefits include:

- Reduced notification spam
- Improved readability
- Better operational awareness

---

## Recovery Alerts

Pulse not only reports failures but also notifies when monitored metrics return to healthy levels.

Recovery alerts help operators confirm that an incident has been resolved without manually checking dashboards.

Example:

```text
CPU usage has returned to normal levels.
Current value: 42%
Status: Healthy
```

---

## Logging

Every alert is recorded through the project's structured logging system.

Logged information includes:

- Metric
- Measured value
- Threshold exceeded
- Time
- Notification status

This provides a historical record of monitoring activity and assists with troubleshooting.

---

## Configuration

Alert behaviour is configured through environment variables.

Typical configuration includes:

- CPU thresholds
- Memory thresholds
- Disk thresholds
- Slack webhook URL
- SMTP server
- Email credentials
- Alert cooldown period

Please refer to `configuration.md` for the complete list of configurable options.

---

## Current Capabilities

The current implementation supports:

- CPU alerts
- Memory alerts
- Disk alerts
- Slack notifications
- Email notifications
- Alert cooldowns
- Recovery alerts
- Structured logging

---

## Future Improvements

The alerting system has been designed to support future enhancements without major architectural changes.

Planned features include:

- Structured alert objects
- Severity levels (Info, Warning, Critical)
- Incident IDs
- Alert history
- Microsoft Teams notifications
- Discord notifications
- Alert acknowledgement
- Escalation policies
- Alert persistence in a database

These features are planned for future Pulse releases as the platform continues to evolve.

---

## Design Principles

The alerting system is built around several core principles.

### Reliability

Alerts should be delivered consistently when important thresholds are exceeded.

### Simplicity

Notifications should contain only the information required to understand the issue quickly.

### Extensibility

New notification providers can be added with minimal changes to the existing monitoring logic.

### Operational Awareness

Alerts should help users understand both when problems occur and when systems recover, providing a complete view of infrastructure health.