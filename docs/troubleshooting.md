# Troubleshooting

## Overview

This guide covers common issues that may occur when running Pulse locally or through Docker Compose.

When troubleshooting Pulse, first check the application logs and the status of the Docker services before changing configuration.

---

## Check Service Status

When running Pulse with Docker Compose:

```bash
docker compose ps
```

The Pulse, Prometheus, and Grafana services should be running.

For more detailed output:

```bash
docker compose logs
```

To inspect a specific service:

```bash
docker compose logs <service-name>
```

---

## Pulse Does Not Start

### Check Python dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Check environment configuration

Confirm that a `.env` file exists and contains the required configuration.

Use `.env.example` as the template.

Never commit the real `.env` file to source control.

### Check application output

Run Pulse directly:

```bash
python3 main.py
```

Review any exception or configuration error displayed in the terminal.

---

## Docker Compose Does Not Start

Validate the Compose configuration:

```bash
docker compose config --quiet
```

If validation succeeds, start the stack:

```bash
docker compose up --build
```

Check running containers:

```bash
docker compose ps
```

Review logs when a container exits unexpectedly:

```bash
docker compose logs
```

---

## Port Already in Use

Pulse services require local ports for the API, Prometheus, and Grafana.

Check which process is using a port:

```bash
lsof -i :8000
```

For Grafana:

```bash
lsof -i :3000
```

For Prometheus:

```bash
lsof -i :9090
```

Stop the conflicting process or change the relevant port mapping before restarting Pulse.

---

## Health Endpoint Is Unavailable

Check:

```bash
curl http://localhost:8000/health
```

If the request fails:

1. Confirm the Pulse container is running.
2. Check the configured API port.
3. Review application logs.
4. Confirm FastAPI started successfully.

Docker users can inspect the service with:

```bash
docker compose logs
```

---

## Metrics Endpoint Is Unavailable

Test:

```bash
curl http://localhost:8000/metrics
```

If `/health` works but `/metrics` does not:

- Confirm the metrics endpoint is registered.
- Review FastAPI logs.
- Check that the required Prometheus client dependency is installed.

---

## Prometheus Target Is Down

Open Prometheus:

```text
http://localhost:9090
```

Check the configured targets.

If Pulse appears as `DOWN`:

1. Confirm the Pulse service is healthy.
2. Verify `/metrics` responds.
3. Check `prometheus.yml`.
4. Confirm Prometheus is using the correct Docker service hostname and port.
5. Restart the stack if configuration has changed.

```bash
docker compose restart
```

---

## Metrics Are Missing From Prometheus

First confirm that Pulse exposes metrics:

```bash
curl http://localhost:8000/metrics
```

Then inspect Prometheus and query one of the Pulse metrics.

If the metric is absent:

- Check the metric name.
- Confirm Prometheus successfully scraped Pulse.
- Review the scrape configuration.
- Check Pulse application logs.

---

## Grafana Cannot Connect to Prometheus

Within Docker Compose, Grafana should communicate with Prometheus through the Docker network rather than through `localhost`.

The Prometheus data source should normally use:

```text
http://prometheus:9090
```

If the connection fails:

1. Confirm Prometheus is running.
2. Check the Grafana data source configuration.
3. Confirm both containers are part of the same Compose stack.
4. Review Grafana and Prometheus logs.

---

## Grafana Panels Show No Data

If Grafana loads but a panel contains no data:

- Confirm Prometheus is receiving Pulse metrics.
- Check the PromQL query used by the panel.
- Increase the dashboard time range.
- Confirm the expected metric name has not changed.
- Check that Pulse has been running long enough to produce data.

---

## Grafana Configuration Disappears After Restart

Pulse uses persistent Grafana storage.

Check that the Grafana volume exists:

```bash
docker volume ls
```

Avoid using:

```bash
docker compose down -v
```

unless you intentionally want to remove persistent volumes.

The `-v` option removes Compose-managed volumes and can therefore remove persisted Grafana data.

---

## Slack Alerts Are Not Received

Check:

- `SLACK_WEBHOOK_URL` is configured.
- The webhook is still active.
- The correct Slack channel is configured.
- Pulse has actually crossed an alert threshold.
- The alert is not currently inside its cooldown period.

Review Pulse logs for notification failures.

Never print or commit the complete webhook URL when debugging.

---

## Email Alerts Are Not Received

Check:

- SMTP server
- SMTP port
- Username
- Password
- Sender address
- Recipient address

Also verify that the email provider permits SMTP access using the configured authentication method.

Review Pulse logs for SMTP errors.

---

## Alerts Are Not Triggering

Confirm:

- Monitoring is running.
- Threshold configuration is loaded.
- The metric actually exceeds its configured threshold.
- Alert cooldown logic is not suppressing a repeated notification.

Review the health and application logs to confirm the current metric state.

---

## Logs Are Missing

Confirm the expected logging directory exists and that the application has permission to write to it.

Current log output may include:

```text
logs/system_health.log
logs/health_log.txt
```

Run Pulse and inspect the terminal for logging-related exceptions.

---

## Resetting the Docker Environment

A normal restart should use:

```bash
docker compose down
docker compose up --build -d
```

For a completely clean Docker reset:

```bash
docker compose down -v
docker compose up --build -d
```

Use the second option carefully because `-v` removes persistent volumes.

---

## Getting More Diagnostic Information

Useful commands include:

```bash
docker compose ps
```

```bash
docker compose logs
```

```bash
docker compose logs --tail=100
```

```bash
curl http://localhost:8000/health
```

```bash
curl http://localhost:8000/metrics
```

These checks help determine whether an issue originates from Pulse, Docker, Prometheus, or Grafana.

---

## Related Documentation

- [Setup](./setup.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Alerting](./alerting.md)