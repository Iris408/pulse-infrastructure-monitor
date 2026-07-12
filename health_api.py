# EN: FastAPI health endpoint for the System Health Monitor
# JP: System Health Monitor 用の FastAPI ヘルスチェックエンドポイント

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


app = FastAPI(
    title="System Health Monitor API",
    description="Healthcheck API for monitoring CPU, memory, disk, and uptime.",
    version="2.0.0",
)


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
        "service": "system-health-monitor",
        "message": "System Health Monitor API is running.",
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
        "service": "system-health-monitor",
        "status": overall_status,
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": uptime,
        "checks": {
            "cpu": format_metric_health("cpu", cpu),
            "memory": format_metric_health("memory", memory),
            "disk": format_metric_health("disk", disk),
        },
    }