# Troubleshooting

## Overview

This guide covers common issues that may occur when running Pulse locally or through Docker Compose.

When troubleshooting Pulse, first determine which part of the stack is affected:

```text
Pulse
  │
  ▼
FastAPI
  │
  ▼
Prometheus
  │
  ▼
Grafana
```

Alerting and logging operate alongside the monitoring stack and may require separate configuration checks.

Before changing application configuration, check:

1. Docker service status
2. Application logs
3. Health and metrics endpoints
4. Prometheus target status
5. Grafana data source connectivity

---

## Check Service Status

When running Pulse with Docker Compose:

```bash
docker compose ps
```

The current Compose services are:

```text
monitor
prometheus
grafana
```

The `monitor` service should report as healthy once its configured health check succeeds.

For logs from the complete stack:

```bash
docker compose logs
```

To inspect a specific service:

```bash
docker compose logs monitor
```

```bash
docker compose logs prometheus
```

```bash
docker compose logs grafana
```

For recent output only:

```bash
docker compose logs --tail=100
```

---

# Pulse Application

## Pulse Does Not Start

### Check Python Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

If using a virtual environment, confirm that it is active before installing dependencies or running Pulse.

---

### Check Environment Configuration

Confirm that a `.env` file exists in the repository root.

Create one from the provided example if necessary:

```bash
cp .env.example .env
```

Update the values required for your local environment.

Never commit the real `.env` file to source control.

See [Configuration](./configuration.md) for configuration details.

---

### Run Pulse Directly

Pulse v2.3.2 uses the modular application structure.

Run the terminal monitor from the repository root with:

```bash
python -m app.main
```

Depending on your Python installation, you may need:

```bash
python3 -m app.main
```

Review any exception or configuration error displayed in the terminal.

Older commands such as:

```text
python3 main.py
```

no longer apply after the v2.3.2 architecture refactor.

---

## FastAPI Does Not Start

Run the FastAPI application directly:

```bash
python -m uvicorn app.api.health:app --reload --port 8000
```

If the application does not start:

- Confirm dependencies are installed.
- Confirm the command is being run from the repository root.
- Check the Python module path.
- Review the exception shown in the terminal.
- Confirm port `8000` is available.

---

# Docker

## Docker Compose Does Not Start

Validate the Compose configuration:

```bash
docker compose config --quiet
```

If validation succeeds, build and start the stack:

```bash
docker compose up --build
```

Check service status:

```bash
docker compose ps
```

Review logs if a container exits unexpectedly:

```bash
docker compose logs
```

---

## Pulse Container Is Unhealthy

The `monitor` service includes a Docker health check against:

```text
http://127.0.0.1:8000/health
```

Check its status:

```bash
docker compose ps
```

Inspect the Pulse service logs:

```bash
docker compose logs monitor
```

You can also test the health endpoint from the host:

```bash
curl http://localhost:8000/health
```

If the container remains unhealthy:

- Confirm FastAPI started successfully.
- Check environment configuration.
- Review the `monitor` service logs.
- Confirm the health endpoint responds successfully.
- Check for application startup errors.

---

## Port Already in Use

Pulse uses the following host ports:

| Service | Port |
| --- | ---: |
| Pulse | `8000` |
| Prometheus | `9090` |
| Grafana | `3000` |

Check which process is using the Pulse API port:

```bash
lsof -i :8000
```

Check Prometheus:

```bash
lsof -i :9090
```

Check Grafana:

```bash
lsof -i :3000
```

Stop the conflicting process or change the relevant Docker port mapping before restarting Pulse.

---

# FastAPI Endpoints

## Health Endpoint Is Unavailable

Test the endpoint:

```bash
curl http://localhost:8000/health
```

If the request fails:

1. Confirm the Pulse service is running.
2. Check whether the `monitor` container is healthy.
3. Confirm port `8000` is available.
4. Review the Pulse logs.
5. Confirm FastAPI started successfully.

Docker users can inspect the service with:

```bash
docker compose logs monitor
```

---

## Metrics Endpoint Is Unavailable

Test:

```bash
curl http://localhost:8000/metrics
```

If `/health` works but `/metrics` does not:

- Confirm the metrics endpoint is registered.
- Review the FastAPI logs.
- Confirm the required dependencies are installed.
- Check for errors when metrics are collected.

Expected Pulse metric names include:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

# Prometheus

## Prometheus Does Not Start

Check the Prometheus service:

```bash
docker compose ps
```

Review its logs:

```bash
docker compose logs prometheus
```

Pulse mounts the Prometheus configuration from:

```text
config/prometheus.yml
```

If Prometheus fails during startup, check the configuration file for invalid syntax or incorrect paths.

---

## Prometheus Target Is Down

Open Prometheus:

```text
http://localhost:9090
```

Navigate to:

```text
Status → Targets
```

The Pulse target should report:

```text
UP
```

If it reports `DOWN`:

1. Confirm the `monitor` service is healthy.
2. Verify `/metrics` responds from the host.
3. Check `config/prometheus.yml`.
4. Confirm the target uses the correct Docker service hostname.
5. Review Prometheus logs.

Within Docker Compose, Prometheus should communicate with Pulse using:

```text
monitor:8000
```

rather than:

```text
localhost:8000
```

The Compose service name `monitor` is available through Docker's internal service networking.

---

## Metrics Are Missing From Prometheus

First confirm that Pulse exposes metrics:

```bash
curl http://localhost:8000/metrics
```

Then open Prometheus:

```text
http://localhost:9090
```

Try querying:

```text
system_cpu_usage_percent
```

```text
system_memory_usage_percent
```

```text
system_disk_usage_percent
```

```text
system_uptime_hours
```

If a metric is absent:

- Confirm the metric name.
- Confirm the Pulse target reports `UP`.
- Review the Prometheus scrape configuration.
- Check the Pulse application logs.
- Review Prometheus logs.

---

# Grafana

## Grafana Cannot Connect to Prometheus

Within Docker Compose, Grafana should communicate with Prometheus through the internal Docker network.

The Prometheus data source should use:

```text
http://prometheus:9090
```

Do not use:

```text
http://localhost:9090
```

from inside the Grafana container.

Inside Grafana, `localhost` refers to the Grafana container itself rather than the Prometheus container.

If the connection fails:

1. Confirm Prometheus is running.
2. Confirm the Prometheus target is healthy.
3. Check the Grafana data source configuration.
4. Review Grafana logs.
5. Review Prometheus logs.

Useful commands:

```bash
docker compose logs grafana
```

```bash
docker compose logs prometheus
```

---

## Grafana Panels Show No Data

If Grafana loads but a panel contains no data:

1. Confirm Prometheus is receiving Pulse metrics.
2. Query the metric directly in Prometheus.
3. Check the PromQL query used by the panel.
4. Increase the Grafana dashboard time range.
5. Confirm the expected metric name has not changed.
6. Confirm Pulse has been running long enough to provide metric data.

Current dashboard metrics include:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

## Grafana Configuration Disappears After Restart

Pulse uses the persistent Docker volume:

```text
grafana_data
```

Check available Docker volumes:

```bash
docker volume ls
```

A normal shutdown using:

```bash
docker compose down
```

preserves Compose-managed volumes.

Avoid:

```bash
docker compose down -v
```

unless you intentionally want to remove persistent data.

The `-v` option removes Compose-managed volumes and can remove persisted Grafana application data, including configured data sources and dashboards.

---

# Alerting

## Slack Alerts Are Not Received

Check:

- Slack webhook configuration is present.
- The webhook is still active.
- The intended Slack channel is associated with the webhook.
- Pulse has actually crossed an alert threshold.
- Cooldown behaviour is not suppressing a repeated alert.

Review Pulse logs:

```bash
docker compose logs monitor
```

Also review the structured application logs where applicable.

Never print, commit, or share the complete Slack webhook URL when debugging.

---

## Email Alerts Are Not Received

Check the configured email settings, including:

- SMTP server
- SMTP port
- Username
- Password or app password
- Sender address
- Recipient address

Also confirm that the email provider permits SMTP access using the configured authentication method.

Review Pulse logs for SMTP or notification errors.

---

## Alerts Are Not Triggering

Confirm:

- Pulse monitoring is running.
- Threshold configuration has loaded correctly.
- The monitored metric actually exceeds the configured threshold.
- Alert configuration is present.
- Cooldown behaviour is not suppressing a repeated notification.

Review the application and structured logs to confirm the current monitoring state.

---

## Repeated Alerts Are Not Being Sent

Pulse implements alert cooldown behaviour.

If an alert has already been sent for an ongoing condition, another notification may be intentionally suppressed until the cooldown period expires.

Check the structured logs for an event such as:

```text
event=alert_skipped
```

with:

```text
reason=cooldown
```

This indicates that Pulse detected the condition but intentionally suppressed another notification.

---

## Recovery Alert Is Not Received

Recovery notifications depend on Pulse previously detecting an unhealthy state and then observing the monitored metric return to a healthy state.

Check:

- An earlier warning or critical state occurred.
- The metric has returned to the configured healthy range.
- Notification configuration is valid.
- Application logs contain the expected recovery behaviour.

Structured logs may contain:

```text
event=recovery_alert_sent
```

---

# Logging

## Logs Are Missing

Current log output may include:

```text
logs/system_health.log
logs/health_log.txt
```

If logs are missing:

- Confirm the expected logging directory exists.
- Confirm the application can write to the directory.
- Run Pulse and inspect the terminal for logging-related errors.
- Review the logging configuration.
- Confirm the expected monitoring behaviour has occurred.

Generated log files should not be committed to source control.

---

# Testing

## Pytest Fails

Run the test suite from the repository root:

```bash
pytest
```

If tests fail:

- Confirm the virtual environment is active.
- Confirm dependencies are installed.
- Confirm the command is being run from the repository root.
- Review the failing test output.
- Check for module import errors after application structure changes.

Pulse v2.3.2 uses application paths under:

```text
app/
```

Older root-level imports may no longer be valid.

---

# Resetting the Docker Environment

## Normal Restart

For a normal restart:

```bash
docker compose down
docker compose up --build -d
```

This preserves persistent volumes.

---

## Complete Reset

For a clean Docker reset:

```bash
docker compose down -v
docker compose up --build -d
```

Use this carefully.

The `-v` option removes Compose-managed volumes and can remove persisted Grafana application data.

---

# Diagnostic Checklist

When the source of a problem is unclear, work through the stack in order.

### 1. Check Docker

```bash
docker compose ps
```

### 2. Check Pulse

```bash
curl http://localhost:8000/health
```

### 3. Check Metrics

```bash
curl http://localhost:8000/metrics
```

### 4. Check Prometheus

Open:

```text
http://localhost:9090
```

Confirm the Pulse target reports:

```text
UP
```

### 5. Query a Metric

For example:

```text
system_cpu_usage_percent
```

### 6. Check Grafana

Open:

```text
http://localhost:3000
```

Confirm the Prometheus data source is reachable and dashboard panels contain data.

### 7. Review Logs

```bash
docker compose logs --tail=100
```

For Pulse specifically:

```bash
docker compose logs monitor --tail=100
```

Following the stack in this order helps isolate whether the problem originates from the Pulse application, FastAPI, Docker, Prometheus, Grafana, or the alerting configuration.

---

## Related Documentation

- [Setup](./setup.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Alerting](./alerting.md)
- [Logging](./logging.md)
- [Architecture](./architecture.md)