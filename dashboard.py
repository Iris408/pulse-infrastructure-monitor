from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from main import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_uptime,
    check_status
)


app = FastAPI()


# EN: Get current system health data
# JP: 現在のシステム状態データを取得
# KR: 현재 시스템 상태 데이터 가져오기

def get_health_data():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    uptime = get_system_uptime()

    return {
        "cpu_usage": cpu_usage,
        "cpu_status": check_status(cpu_usage),
        "memory_usage": memory_usage,
        "memory_status": check_status(memory_usage),
        "disk_usage": disk_usage,
        "disk_status": check_status(disk_usage),
        "uptime_hours": uptime
    }


# EN: API endpoint for system health data
# JP: システム状態データ用APIエンドポイント
# KR: 시스템 상태 데이터 API 엔드포인트

@app.get("/health")
def health():
    return get_health_data()


# EN: Simple web dashboard
# JP: シンプルなWebダッシュボード
# KR: 간단한 웹 대시보드

@app.get("/", response_class=HTMLResponse)
def dashboard():
    data = get_health_data()

    html = f"""
    <html>
        <head>
            <title>Pulse</title>
        </head>

        <body>
            <h1>Infrastructure Health Monitoring Platform</h1>

            <h2>Current Metrics</h2>

            <p><strong>CPU Usage:</strong> {data["cpu_usage"]}%</p>
            <p><strong>CPU Status:</strong> {data["cpu_status"]}</p>

            <p><strong>Memory Usage:</strong> {data["memory_usage"]}%</p>
            <p><strong>Memory Status:</strong> {data["memory_status"]}</p>

            <p><strong>Disk Usage:</strong> {data["disk_usage"]}%</p>
            <p><strong>Disk Status:</strong> {data["disk_status"]}</p>

            <p><strong>System Uptime:</strong> {data["uptime_hours"]} hours</p>
        </body>
    </html>
    """

    return html
