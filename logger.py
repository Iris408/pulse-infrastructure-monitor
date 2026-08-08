# EN: Structured logging helpers for Infrastructure Health Monitoring Platform
# JP: Infrastructure Health Monitoring Platform 用の構造化ログヘルパー

import logging
import os


LOG_DIR = "logs"
STRUCTURED_LOG_FILE = os.path.join(LOG_DIR, "pulse.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("pulse_monitor")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(STRUCTURED_LOG_FILE)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def format_log_fields(**fields):
    # EN: Convert key-value data into a readable structured log format
    # JP: キーと値のデータを読みやすい構造化ログ形式に変換します

    formatted_fields = []

    for key, value in fields.items():
        if value is not None:
            formatted_fields.append(f"{key}={value}")

    return " | ".join(formatted_fields)


def log_event(level, event_name, **fields):
    # EN: Write one structured event to the log file
    # JP: 1つの構造化イベントをログファイルに書き込みます

    message = f"event={event_name}"

    formatted_fields = format_log_fields(**fields)

    if formatted_fields:
        message = f"{message} | {formatted_fields}"

    if level == "warning":
        logger.warning(message)

    elif level == "error":
        logger.error(message)

    else:
        logger.info(message)


def log_metric_status(metric, value, status_level, status_message):
    log_event(
        "info",
        "metric_check",
        metric=metric,
        value=value,
        status_level=status_level,
        status_message=status_message,
    )


def log_alert_sent(metric, value, status_level, channel):
    log_event(
        "warning",
        "alert_sent",
        metric=metric,
        value=value,
        status_level=status_level,
        channel=channel,
    )


def log_alert_skipped(metric, value, status_level, reason):
    log_event(
        "info",
        "alert_skipped",
        metric=metric,
        value=value,
        status_level=status_level,
        reason=reason,
    )


def log_recovery_sent(metric, value, previous_level):
    log_event(
        "info",
        "recovery_alert_sent",
        metric=metric,
        value=value,
        previous_level=previous_level,
        status_level="OK",
    )


# =========================================
# EN: Backwards-compatible helper functions
# JP: 既存コードとの互換性を保つためのヘルパー関数
# =========================================

def log_status(message):
    log_event(
        "info",
        "status",
        message=message,
    )


def log_alert(message):
    log_event(
        "warning",
        "alert",
        message=message,
    )