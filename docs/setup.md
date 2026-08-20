# Setup Guide

## Overview

Pulse can be run directly with Python or as a containerised monitoring stack using Docker Compose.

The Docker Compose environment provides the complete monitoring stack:

- Pulse
- Prometheus
- Grafana

Pulse v2.3.2 uses a modular Python application structure, with application code organised under `app/` and monitoring configuration stored under `config/`.

---

## Prerequisites

For local Python development:

- Python 3.11+
- pip
- Git

For the complete monitoring stack:

- Docker
- Docker Compose

---

## Clone the Repository

```bash
git clone https://github.com/Iris408/pulse-infrastructure-monitor.git
cd pulse-infrastructure-monitor
```

---

## Environment Configuration

Create a local environment file from the provided example:

```bash
cp .env.example .env
```

Update the values required for your environment.

The `.env` file may contain sensitive information and should not be committed to Git.

See [Configuration Documentation](./configuration.md) for detailed configuration information.

---

# Local Python Setup

## Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the Terminal Monitor

From the repository root:

```bash
python -m app.main
```
> **Python command note:** Depending on your operating system and Python installation, the Python command may be `python` or `python3`. If a command using `python` is not recognised, try the equivalent command with `python3`.

---

## Run the FastAPI Application

From the repository root:

```bash
python -m uvicorn app.api.health:app --reload --port 8000
```

The API is then available locally.

### Root

```text
http://localhost:8000/
```

### Health

```text
http://localhost:8000/health
```

### Metrics

```text
http://localhost:8000/metrics
```

### Swagger

```text
http://localhost:8000/docs
```

---

## Run Automated Tests

Pulse uses pytest for backend testing.

Run the test suite from the repository root:

```bash
pytest
```

Pytest configuration is stored in:

```text
pytest.ini
```

The current test suite includes FastAPI health and metrics endpoint checks.

---

# Docker Setup

For the complete Pulse monitoring environment:

```bash
docker compose up --build
```

To run in the background:

```bash
docker compose up --build -d
```

Check service status:

```bash
docker compose ps
```

The Pulse API container should report as healthy once its health check succeeds.

---

## Verify Pulse

Check application health:

```bash
curl http://localhost:8000/health
```

Check Prometheus-compatible metrics:

```bash
curl http://localhost:8000/metrics
```

---

## Prometheus

Prometheus is available at:

```text
http://localhost:9090
```

The Prometheus configuration is stored at:

```text
config/prometheus.yml
```

Docker Compose mounts this configuration into the Prometheus container.

Confirm that the Pulse target is being scraped successfully and reports as `UP`.

Pulse currently exposes:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

## Grafana

Grafana is available at:

```text
http://localhost:3000
```

Grafana uses Prometheus as the monitoring data source and provides dashboard visualisation for:

- CPU usage
- Memory usage
- Disk usage
- System uptime

See [Grafana Dashboard Documentation](./grafana-dashboard.md) for additional dashboard information.

### Grafana Persistent Data

Grafana data is persisted using the Docker Compose volume:

```text
grafana_data
```

This allows Grafana configuration and dashboard data to survive normal container restarts.

Running:

```bash
docker compose down
```

preserves this volume.

Running:

```bash
docker compose down -v
```

removes Compose-managed volumes and may remove persisted Grafana configuration.

If the Grafana data is reset, the Prometheus data source and Pulse dashboard may need to be recreated or re-imported.

When Grafana and Prometheus are running through Docker Compose, the Prometheus data source should use the internal service address:

```text
http://prometheus:9090
```

rather than `localhost:9090`.

---

# Stopping Pulse

Stop the Docker Compose environment:

```bash
docker compose down
```

This preserves persistent volumes.

---

## Complete Reset

To stop Pulse and remove Compose-managed volumes:

```bash
docker compose down -v
```

Use this carefully because persisted Grafana configuration may be removed.

---

# Development Verification

Before committing changes, perform the checks relevant to the change.

Run the backend tests:

```bash
pytest
```

Validate Docker Compose:

```bash
docker compose config --quiet
```

Verify the health endpoint:

```bash
curl http://localhost:8000/health
```

Verify metrics:

```bash
curl http://localhost:8000/metrics
```

Review container status:

```bash
docker compose ps
```

For monitoring-stack changes, also confirm:

- Pulse reports as healthy
- Prometheus reports the Pulse target as `UP`
- Grafana can query Prometheus
- CPU, memory, disk, and uptime panels receive data

---

# Current Application Paths

Pulse v2.3.2 introduced a modular application structure.

Key paths include:

```text
app/main.py
app/api/health.py
app/monitoring/
app/alerts/
app/logging/
app/dashboard/
config/prometheus.yml
tests/
pytest.ini
```

Older commands referencing root-level modules such as `main.py` or `health_api.py` no longer apply after the v2.3.2 refactor.

---

# Common Problems

If Pulse, Prometheus, Grafana, alerts, or metrics are not working as expected, see [Troubleshooting](./troubleshooting.md).

Common areas to check include:

- Python module paths
- Environment configuration
- Docker container health
- Prometheus target status
- Grafana data source configuration
- Port conflicts
- Alert credentials

---

## Related Documentation

- [Architecture](./architecture.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Troubleshooting](./troubleshooting.md)