# Monitoring Stack

This document explains the monitoring stack used by the System Health Monitor project.

The stack includes:

- FastAPI `/health` endpoint
- FastAPI `/metrics` endpoint
- Prometheus scrape configuration
- Grafana dashboard panels
- Docker Compose services

---

## Services

| Service | URL | Purpose |
| --- | --- | --- |
| System Health Monitor API | http://localhost:8000 | FastAPI health and metrics API |
| Prometheus | http://localhost:9090 | Scrapes `/metrics` from the monitor service |
| Grafana | http://localhost:3000 | Visualizes Prometheus metrics |

---

## FastAPI Endpoints

### Health endpoint

```bash
curl http://127.0.0.1:8000/health
```

Returns CPU, memory, disk, uptime, and overall status.

### Metrics endpoint

```bash
curl http://127.0.0.1:8000/metrics
```

Returns Prometheus-compatible metrics.

Example metrics:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

## Prometheus

Prometheus uses `prometheus.yml` to scrape the FastAPI `/metrics` endpoint.

The target inside Docker Compose is:

```text
monitor:8000
```

Prometheus UI:

```text
http://localhost:9090
```

To check the scrape target:

```text
Status → Targets
```

Expected result:

```text
system-health-monitor UP
```

Example queries:

```text
system_cpu_usage_percent
system_memory_usage_percent
system_disk_usage_percent
system_uptime_hours
```

---

## Grafana

Grafana runs through Docker Compose and connects to Prometheus.

Grafana URL:

```text
http://localhost:3000
```

Default local login:

```text
Username: admin
Password: admin
```

Prometheus data source URL:

```text
http://prometheus:9090
```

---

## Grafana Dashboard

Dashboard name:

```text
System Health Monitor Dashboard
```

Current panels:

| Panel | Prometheus Query | Visualization |
| --- | --- | --- |
| CPU Usage | `system_cpu_usage_percent` | Gauge |
| Memory Usage | `system_memory_usage_percent` | Gauge |
| Disk Usage | `system_disk_usage_percent` | Gauge |
| System Uptime | `system_uptime_hours` | Stat |

Recommended layout:

```text
[ CPU Usage ]     [ Memory Usage ]

[ Disk Usage ]    [ System Uptime ]
```

---

## Running the Stack

Start all services:

```bash
docker compose up --build
```

Run in the background:

```bash
docker compose up -d
```

Stop all services:

```bash
docker compose down
```

---

## Docker Compose Services

The stack includes:

```text
monitor
prometheus
grafana
```

Grafana uses a persistent Docker volume:

```text
grafana_data
```

This keeps the Grafana data source and dashboard saved after container restarts.

---

## Current Status

| Feature | Status |
| --- | --- |
| FastAPI `/health` endpoint | Complete |
| FastAPI `/metrics` endpoint | Complete |
| Prometheus scrape configuration | Complete |
| Grafana Docker service | Complete |
| Grafana persistent volume | Complete |
| Basic Grafana dashboard panels | Complete |

---

## Next Improvements

- Export/provision Grafana dashboard configuration
- Add automated tests
- Add alert history storage
- Add `/alerts` endpoint
- Add architecture diagram
- Add PostgreSQL or SQLite alert storage