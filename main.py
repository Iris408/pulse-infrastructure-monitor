import os
import time
from datetime import datetime

import psutil
from colorama import Fore, Style, init
from dotenv import load_dotenv

from alerts import send_slack_alert
from email_alerts import send_email_alert
from logger import log_status, log_alert


# =========================================
# EN: Load environment variables from .env
# JP: .env から環境変数を読み込みます
# KR: .env에서 환경 변수를 불러옵니다
# =========================================

load_dotenv()


# =========================================
# EN: Initialize colorama for coloured terminal output
# JP: ターミナルの色付き出力のために colorama を初期化します
# KR: 터미널 색상 출력을 위해 colorama를 초기화합니다
# =========================================

init(autoreset=True)


# =========================================
# EN: File path for saved health logs
# JP: 保存されるヘルスログのファイルパス
# KR: 저장되는 상태 로그 파일 경로
# =========================================

LOG_FILE = "logs/health_log.txt"


# =========================================
# EN: Load configurable monitoring settings from environment variables
# JP: 環境変数から変更可能な監視設定を読み込みます
# KR: 환경 변수에서 설정 가능한 모니터링 값을 불러옵니다
#
# NOTE:
# EN: REFRESH_INTERVAL is in seconds. 300 seconds = 5 minutes.
# JP: REFRESH_INTERVAL は秒単位です。300秒 = 5分です。
# KR: REFRESH_INTERVAL은 초 단위입니다. 300초 = 5분입니다.
# =========================================

OK_THRESHOLD = int(os.getenv("OK_THRESHOLD", 45))
WARNING_THRESHOLD = int(os.getenv("WARNING_THRESHOLD", 75))
CRITICAL_THRESHOLD = int(os.getenv("CRITICAL_THRESHOLD", 95))
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", 300))

ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", 1800))

last_alert_times = {
    "cpu": 0,
    "memory": 0,
    "disk": 0,
}

# =========================================
# EN: Get current CPU usage percentage
# JP: 現在の CPU 使用率を取得します
# KR: 현재 CPU 사용률을 가져옵니다
# =========================================

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


# =========================================
# EN: Get current memory usage percentage
# JP: 現在のメモリ使用率を取得します
# KR: 현재 메모리 사용률을 가져옵니다
# =========================================

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


# =========================================
# EN: Get current disk usage percentage
# JP: 現在のディスク使用率を取得します
# KR: 현재 디스크 사용률을 가져옵니다
# =========================================

def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent


# =========================================
# EN: Get system uptime in hours
# JP: システム稼働時間を時間単位で取得します
# KR: 시스템 가동 시간을 시간 단위로 가져옵니다
# =========================================

def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    return int(uptime_hours)


# =========================================
# EN: Check usage status based on thresholds
# JP: しきい値に基づいて使用状況を確認します
# KR: 임계값을 기준으로 사용 상태를 확인합니다
# =========================================

def check_status(value):
    if value >= CRITICAL_THRESHOLD:
        return f"CRITICAL: Usage is over {CRITICAL_THRESHOLD}%"

    elif value >= WARNING_THRESHOLD:
        return f"WARNING: Usage is over {WARNING_THRESHOLD}%"

    else:
        return f"OK: Usage is below {WARNING_THRESHOLD}%"


# =========================================
# EN: Choose terminal colour based on status
# JP: ステータスに基づいてターミナルの色を選択します
# KR: 상태에 따라 터미널 색상을 선택합니다
# =========================================

def get_status_color(status):
    if "OK" in status:
        return Fore.GREEN

    elif "WARNING" in status:
        return Fore.YELLOW

    else:
        return Fore.RED


# =========================================
# EN: Save one health check entry to the log file
# JP: 1回分のヘルスチェックをログファイルに保存します
# KR: 한 번의 상태 확인 결과를 로그 파일에 저장합니다
# =========================================

def save_to_log(entry):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(entry + "\n")


# =========================================
# EN: Create a simple visual usage bar
# JP: シンプルな使用率バーを作成します
# KR: 간단한 사용량 표시 막대를 만듭니다
# =========================================

def create_usage_bar(value, bar_length=10):
    filled_length = int(bar_length * value / 100)
    empty_length = bar_length - filled_length

    return "█" * filled_length + "-" * empty_length


# =========================================
# EN: Display one metric in the terminal
# JP: 1つのメトリックをターミナルに表示します
# KR: 하나의 메트릭을 터미널에 표시합니다
# =========================================

def display_metric(name, value):
    status = check_status(value)
    color = get_status_color(status)
    bar = create_usage_bar(value)

    print(
        f"{name}: {value}% "
        f"[{color}{bar}{Style.RESET_ALL}] "
        f"{color}[{status}]{Style.RESET_ALL}"
    )

    return f"{name}: {value}% [{status}]"

# =========================================
# EN: Check whether an alert can be sent again
# JP: アラートを再送信できるか確認します
# KR: 알림을 다시 보낼 수 있는지 확인합니다
# =========================================

def can_send_alert(alert_type):
    current_time = time.time()
    last_sent_time = last_alert_times[alert_type]

    return current_time - last_sent_time >= ALERT_COOLDOWN_SECONDS

# =========================================
# EN: Update the last sent time for an alert
# JP: アラートの最終送信時刻を更新します
# KR: 알림의 마지막 전송 시간을 업데이트합니다
# =========================================

def update_alert_time(alert_type):
    last_alert_times[alert_type] = time.time()

# =========================================
# EN: Send alerts when system usage is too high
# JP: システム使用率が高すぎる場合にアラートを送信します
# KR: 시스템 사용량이 너무 높을 때 알림을 보냅니다
# =========================================

def handle_alerts(cpu, memory, disk):
    cpu_status = check_status(cpu)
    memory_status = check_status(memory)
    disk_status = check_status(disk)

    if "WARNING" in cpu_status or "CRITICAL" in cpu_status:
        log_alert(f"CPU: {cpu}% - {cpu_status}")
        send_slack_alert(f"CPU ALERT: {cpu}% - {cpu_status}")
        update_alert_time("cpu")

    if "WARNING" in memory_status or "CRITICAL" in memory_status:
        log_alert(f"Memory: {memory}% - {memory_status}")
        send_slack_alert(f"MEMORY ALERT: {memory}% - {memory_status}")
        send_email_alert(
            "Memory Alert",
            f"Memory status triggered an alert: {memory}% - {memory_status}"
        )
        update_alert_time("memory")

    if "WARNING" in disk_status or "CRITICAL" in disk_status:
        log_alert(f"Disk: {disk}% - {disk_status}")
        send_slack_alert(f"DISK ALERT: {disk}% - {disk_status}")
        send_email_alert(
            "Disk Alert",
            f"Disk status triggered an alert: {disk}% - {disk_status}"
        )
        update_alert_time("disk")


# =========================================
# EN: Display full system health report
# JP: システム全体のヘルスレポートを表示します
# KR: 전체 시스템 상태 보고서를 표시합니다
# =========================================

def display_system_health():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    uptime = get_system_uptime()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nSystem Health Monitor")
    print("-----------------------------")
    print(f"Checked At: {current_time}")

    cpu_log = display_metric("CPU Usage", cpu)
    memory_log = display_metric("Memory Usage", memory)
    disk_log = display_metric("Disk Usage", disk)

    print(f"System Uptime: {uptime} hours")

    log_status(f"CPU: {cpu}% - {check_status(cpu)}")
    log_status(f"Memory: {memory}% - {check_status(memory)}")
    log_status(f"Disk: {disk}% - {check_status(disk)}")

    handle_alerts(cpu, memory, disk)

    log_entry = (
        f"{current_time} | "
        f"{cpu_log} | "
        f"{memory_log} | "
        f"{disk_log} | "
        f"Uptime: {uptime} hours"
    )

    save_to_log(log_entry)


# =========================================
# EN: Clear terminal screen when supported
# JP: 対応している場合、ターミナル画面をクリアします
# KR: 지원되는 경우 터미널 화면을 지웁니다
# =========================================

def clear_terminal():
    if os.getenv("TERM"):
        os.system("clear")


# =========================================
# EN: Main automated monitoring loop
# JP: メインの自動監視ループ
# KR: 메인 자동 모니터링 루프
#
# NOTE:
# EN: Press CTRL + C to stop the monitor.
# JP: 監視を停止するには CTRL + C を押します。
# KR: 모니터링을 중지하려면 CTRL + C를 누릅니다.
# =========================================

def main():
    try:
        while True:
            clear_terminal()

            print(Fore.CYAN + "System Health Monitor")
            print("-----------------------------")

            display_system_health()

            time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        print("\nSystem Health Monitor stopped.")


if __name__ == "__main__":
    main()