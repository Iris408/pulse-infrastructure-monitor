# EN: FastAPI health endpoint for the Infrastructure Health Monitoring Platform
# JP: Infrastructure Health Monitoring Platform 用の FastAPI ヘルスチェックエンドポイント

from datetime import datetime

from fastapi import FastAPI

from main import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_uptime,
    get_status_level,
    check_status,
)

from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, Gauge, generate_latest

app = FastAPI(
    title="Pulse Monitor",
    description="Healthcheck API for monitoring CPU, memory, disk, and uptime.",
    version="2.3.2",
)

cpu_gauge = Gauge("system_cpu_usage_percent", "CPU usage percentage")
memory_gauge = Gauge("system_memory_usage_percent", "Memory usage percentage")
disk_gauge = Gauge("system_disk_usage_percent", "Disk usage percentage")
uptime_gauge = Gauge("system_uptime_hours", "System uptime in hours")


def update_prometheus_metrics():
    cpu_gauge.set(get_cpu_usage())
    memory_gauge.set(get_memory_usage())
    disk_gauge.set(get_disk_usage())
    uptime_gauge.set(get_system_uptime())


def format_metric_health(name, value):
    # EN: Convert one metric into a structured health response
    # JP: 1つのメトリックを構造化されたヘルスレスポンスに変換します

    status_level = get_status_level(value)

    return {
        "metric": name,
        "value": value,
        "status_level": status_level,
        "status_message": check_status(value),
    }


@app.get("/")
def root():
    return {
        "service": "pulse-monitor",
        "message": "Pulse Monitor is running.",
        "health_endpoint": "/health",
    }


@app.get("/health")
def health_check():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    uptime = get_system_uptime()

    cpu_status = get_status_level(cpu)
    memory_status = get_status_level(memory)
    disk_status = get_status_level(disk)

    has_critical_issue = "CRITICAL" in [
        cpu_status,
        memory_status,
        disk_status,
    ]

    has_warning_issue = "WARNING" in [
        cpu_status,
        memory_status,
        disk_status,
    ]

    if has_critical_issue:
        overall_status = "critical"

    elif has_warning_issue:
        overall_status = "warning"

    else:
        overall_status = "ok"

    return {
        "service": "pulse-monitor",
        "status": overall_status,
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": uptime,
        "checks": {
            "cpu": format_metric_health("cpu", cpu),
            "memory": format_metric_health("memory", memory),
            "disk": format_metric_health("disk", disk),
        },
    }

@app.get("/metrics")
def prometheus_metrics():
    update_prometheus_metrics()

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )