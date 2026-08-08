# Setup Guide

## Overview

Pulse can be run directly with Python or as a containerised monitoring stack using Docker Compose.

The Docker Compose environment provides the complete monitoring stack:

- Pulse
- Prometheus
- Grafana

---

## Prerequisites

For local Python development:

- Python 3
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

See:

[Configuration Documentation](./configuration.md)

for detailed configuration information.

---

# Local Python Setup

## Create a Virtual Environment

```bash
python3 -m venv .venv
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

```bash
python3 main.py
```

---

## Run the FastAPI Application

```bash
python3 -m uvicorn health_api:app --reload --port 8000
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

---

## Verify Pulse

Check application health:

```bash
curl http://localhost:8000/health
```

Check Prometheus metrics:

```bash
curl http://localhost:8000/metrics
```

---

## Prometheus

Prometheus is available at:

```text
http://localhost:9090
```

Confirm that the Pulse target is being scraped successfully.

---

## Grafana

Grafana is available at:

```text
http://localhost:3000
```

Grafana uses Prometheus as the monitoring data source.

See:

[Grafana Dashboard Documentation](./grafana-dashboard.md)

for additional information.

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

---

# Common Problems

If Pulse, Prometheus, Grafana, alerts, or metrics are not working as expected, see:

[Troubleshooting](./troubleshooting.md)

---

## Related Documentation

- [Architecture](./architecture.md)
- [Configuration](./configuration.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Troubleshooting](./troubleshooting.md)