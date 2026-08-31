# Setup Guide

## Overview

Pulse can be run directly with Python or as a complete containerised monitoring and observability stack using Docker Compose.

The Docker Compose environment runs three services:

- Pulse (`monitor`)
- Prometheus (`prometheus`)
- Grafana (`grafana`)

Pulse v2.3.2 uses a modular Python application structure, with application code organised under `app/` and monitoring configuration stored under `config/`.

---

## Prerequisites

### Local Python Development

- Python 3.11+
- pip
- Git

### Complete Monitoring Stack

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

The `.env` file may contain sensitive configuration and should not be committed to Git.

See [Configuration Documentation](./configuration.md) for detailed configuration information.

---

# Local Python Setup

## Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Depending on your operating system and Python installation, the Python command may be `python` or `python3`.

---

## Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Terminal Monitor

From the repository root:

```bash
python -m app.main
```

This starts the local Pulse monitoring process.

---

## Run the FastAPI Application

From the repository root:

```bash
python -m uvicorn app.api.health:app --reload --port 8000
```

The API is then available locally.

### API Root

```text
http://localhost:8000/
```

### Health Endpoint

```text
http://localhost:8000/health
```

### Metrics Endpoint

```text
http://localhost:8000/metrics
```

### Swagger UI

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

Docker Compose runs the complete Pulse monitoring stack.

Current services:

```text
monitor
prometheus
grafana
```

Build and start the stack:

```bash
docker compose up --build
```

To run the services in the background:

```bash
docker compose up --build -d
```

Check service status:

```bash
docker compose ps
```

The Pulse `monitor` service should report as healthy after its configured health check succeeds.

---

## Pulse Health Check

The `monitor` service includes a Docker health check against:

```text
http://127.0.0.1:8000/health
```

The current health check runs every 30 seconds after an initial start period.

You can also verify the endpoint manually:

```bash
curl http://localhost:8000/health
```

---

## Verify Metrics

Check the Prometheus-compatible metrics endpoint:

```bash
curl http://localhost:8000/metrics
```

Pulse currently exposes metrics including:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

# Prometheus

Prometheus is available locally at:

```text
http://localhost:9090
```

The Prometheus configuration is stored at:

```text
config/prometheus.yml
```

Docker Compose mounts this file into the Prometheus container as its configuration.

Prometheus depends on the Pulse `monitor` service becoming healthy before it starts.

---

## Verify the Prometheus Target

Open Prometheus:

```text
http://localhost:9090
```

Navigate to:

```text
Status → Targets
```

Confirm that the Pulse target reports:

```text
UP
```

Within the Docker Compose network, Prometheus communicates with Pulse using the `monitor` service name.

The target therefore uses:

```text
monitor:8000
```

rather than `localhost:8000`.

---

## Query Pulse Metrics

Example Prometheus queries:

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

Each query should return metric data while the Pulse service is running and being successfully scraped.

---

# Grafana

Grafana is available locally at:

```text
http://localhost:3000
```

Grafana uses Prometheus as its monitoring data source and provides dashboard visualisation for:

- CPU usage
- Memory usage
- Disk usage
- System uptime

See [Grafana Dashboard Documentation](./grafana-dashboard.md) for additional dashboard information.

---

## Prometheus Data Source

When Grafana and Prometheus are running through Docker Compose, the Prometheus data source should use:

```text
http://prometheus:9090
```

The Docker Compose service name allows Grafana to communicate with Prometheus through the internal container network.

Do not use:

```text
http://localhost:9090
```

from inside the Grafana container, because `localhost` would refer to the Grafana container itself.

---

## Grafana Persistent Data

Grafana application data is persisted using the Docker Compose volume:

```text
grafana_data
```

The volume is mounted to:

```text
/var/lib/grafana
```

This allows Grafana application data, including configured data sources and dashboards, to survive normal container restarts.

Running:

```bash
docker compose down
```

preserves the volume.

Running:

```bash
docker compose down -v
```

removes Compose-managed volumes and can remove persisted Grafana configuration.

If Grafana data is reset, the Prometheus data source and Pulse dashboard may need to be recreated or re-imported.

---

# Stopping Pulse

Stop the Docker Compose environment:

```bash
docker compose down
```

This stops the services while preserving persistent volumes.

---

## Complete Reset

To stop Pulse and remove Compose-managed volumes:

```bash
docker compose down -v
```

Use this carefully because persisted Grafana application data may be removed.

---

# Development Verification

Before committing changes, run the checks relevant to the change.

## Backend Tests

```bash
pytest
```

## Docker Compose Validation

```bash
docker compose config --quiet
```

## Health Endpoint

```bash
curl http://localhost:8000/health
```

## Metrics Endpoint

```bash
curl http://localhost:8000/metrics
```

## Container Status

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

Pulse v2.3.2 uses a modular application structure.

Key paths include:

```text
app/
├── api/
├── monitoring/
├── alerts/
├── logging/
└── dashboard/

config/
└── prometheus.yml

tests/
pytest.ini
```

Important application entry points include:

```text
app/main.py
app/api/health.py
```

Older commands referencing root-level modules such as:

```text
main.py
health_api.py
```

no longer apply after the v2.3.2 modular architecture refactor.

---

# Docker Compose Structure

The current Docker Compose stack contains:

```text
monitor
prometheus
grafana
```

The service relationship is:

```text
monitor
   │
   │ health check
   ▼
healthy
   │
   ▼
prometheus
   │
   ▼
grafana
```

Prometheus waits for the `monitor` service health check to succeed.

Grafana depends on the Prometheus service.

The stack exposes:

| Service | Host Port |
| --- | ---: |
| Pulse | `8000` |
| Prometheus | `9090` |
| Grafana | `3000` |

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

# Maintenance

The setup process is considered stable for the current Pulse feature scope.

Future setup-related changes should primarily support maintenance, including:

- Dependency updates
- Python version updates
- Docker image updates
- Docker validation
- CI improvements
- Configuration validation
- Security improvements
- Documentation corrections

Large deployment or infrastructure expansion is outside the current Pulse scope.

---

## Related Documentation

- [Architecture](./architecture.md)
- [Alerting](./alerting.md)
- [Configuration](./configuration.md)
- [Grafana Dashboard](./grafana-dashboard.md)
- [Monitoring Stack](./monitoring-stack.md)
- [Roadmap](./roadmap.md)
- [Troubleshooting](./troubleshooting.md)