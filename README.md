![Backend CI](https://github.com/Iris408/system-health-monitor/actions/workflows/backend-ci.yml/badge.svg)

# System Health Monitor / システム健全性監視

A Python-based system monitoring application that tracks CPU, memory, disk usage, and uptime with threshold-based alerts, logging, Docker support, and a FastAPI dashboard.

CPU、メモリ、ディスク使用量、稼働時間を監視するPythonベースのシステム監視アプリケーションです。しきい値に基づくアラート、ログ記録、Docker対応、FastAPIダッシュボードを備えています。

## Screenshot / スクリーンショット

<img src="./screenshots/system-health-monitor.png" width="500"/>

## Recent Update

### Alert Cooldown

The monitor includes configurable alert cooldown logic to reduce repeated notifications.

Cooldown is tracked separately for CPU, memory, and disk alerts. Warning and critical alerts are also tracked separately, so a new critical alert can still be sent even if a warning alert was recently triggered.

When a metric returns to an OK state, the monitor sends a recovery message once.

## Automation / 自動化

System Health Monitor runs automated checks on a configurable refresh interval.

By default, the monitor checks CPU, memory, disk usage, and uptime every 5 minutes.

**日本語**:  
System Health Monitor は、設定可能な更新間隔で自動的にシステム状態を確認します。

デフォルトでは、CPU、メモリ、ディスク使用量、稼働時間を5分ごとに監視します。

| Setting | Default | Description | 日本語 |
| --- | --- | --- | --- |
| `REFRESH_INTERVAL` | `300` | Runs checks every 300 seconds / 5 minutes | 300秒 / 5分ごとに監視を実行 |
| `WARNING_THRESHOLD` | `75` | Sends a warning when usage is high | 使用率が高い場合に警告 |
| `CRITICAL_THRESHOLD` | `95` | Sends a critical alert when usage is very high | 使用率が非常に高い場合に重大アラート |
| `ALERT_COOLDOWN_SECONDS` | `1800` | Prevents repeated alerts from being sent too often | 同じアラートの連続送信を防止 |

## Features | 機能 

| English | 日本語 | Status |
| --- | --- | --- |
| CPU, memory, disk, and uptime monitoring | CPU、メモリ、ディスク、稼働時間の監視 | ✅ Complete |
| Warning and critical threshold detection | 警告および重大なしきい値の検出 | ✅ Complete |
| Slack alert integration | Slackアラートとの連携 | ✅ Complete |
| Email alert integration | メールアラートとの連携 | ✅ Complete |
| Logging support | ログ記録のサポート | ✅ Complete |
| Docker container support | Dockerコンテナのサポート | ✅ Complete |
| FastAPI web dashboard | FastAPIウェブダッシュボード | ✅ Complete |
| `/health` JSON endpoint | `/health` JSONエンドポイント | ✅ Complete |
| Configurable thresholds using environment variables | 環境変数によるしきい値の設定 | ✅ Complete |
| Configurable alert cooldown | 設定可能なアラートクールダウン | ✅ Complete |
| Separate cooldown tracking for CPU, memory, and disk | CPU、メモリ、ディスクごとの個別クールダウン管理 | ✅ Complete |
| Recovery alert when a metric returns to OK | メトリックがOK状態に戻った時の回復アラート | ✅ Complete |
| EN/JP code comments for learning and review | 学習と復習のための英語/日本語コードコメント | ✅ Complete |
| GitHub Actions CI | GitHub Actions CI | ✅ Complete |

## CI/CD

This project uses GitHub Actions to run automated checks on every push and pull request.

Current pipeline:

- Install Python dependencies
- Validate Python syntax
- Run tests when available
- Build the Docker image when a Dockerfile is present

### Next Roadmap

- Add alert history storage
- Add `/alerts` endpoint
- Improve dashboard layout
- Add architecture diagram
- Add automated tests
- Add PostgreSQL or SQLite alert storage

## Planned Features | 追加予定の機能

- Dashboard UI improvements | ダッシュボードのUI改善 | 🚧 Planned 
- Add automated tests | 自動テストを追加 | 🚧 Planned 
- Add historical monitoring charts | 履歴監視チャートを追加 | 🚧 Planned 
- Add log filtering | ログフィルタリングを追加 | 🚧 Planned 
- Add deployment documentation | デプロイメントドキュメントを追加 | 🚧 Planned 

## Sample Log Output / サンプルログ出力
A safe sample monitoring log is available here:
```text
examples/health_log.txt
```
This sample file is included for demonstration purposes. Real runtime logs are stored locally in the logs/ folder and are excluded from Git.

デモ用の安全な監視ログサンプルは以下に配置しています。
```text
examples/health_log.txt
```
実行時に生成される実際のログは logs/ フォルダに保存されますが、ローカル環境の情報を含む可能性があるため、Git管理から除外しています。

## Environment Variables / 環境変数

This project uses environment variables for alerting, threshold configuration, and automated refresh timing.

**日本語**:  
このプロジェクトでは、アラート設定、しきい値設定、自動更新間隔のために環境変数を使用します。

Create a `.env` file in the project root:

```env
SLACK_WEBHOOK_URL=your_slack_webhook_url
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient@example.com

OK_THRESHOLD=45
WARNING_THRESHOLD=75
CRITICAL_THRESHOLD=95
REFRESH_INTERVAL=300
ALERT_COOLDOWN_SECONDS=1800
```

# Installation / インストール

Clone the repository/ リポジトリのクローン:
```bash
git clone https://github.com/Iris408/system-health-monitor.git
cd system-health-monitor
```
Install dependencies/ 依存関係のインストール:
```bash
pip install -r requirements.txt
```
Run the monitor/ 監視スクリプトの実行:
```bash
python3 main.py
```

## Docker Usage / Dockerでの起動

This project can run inside a Docker container using Docker Compose.

**日本語**:Docker Composeを使用してDockerコンテナ内で実行できます。

Build and run the container/ ビルドして起動:
```bash
docker compose up --build
```
Run in the background/ バックグラウンドで起動:
```bash
docker compose up -d
```
View logs/ ログの確認:
```bash
docker compose logs
```
Stop the container/ コンテナの停止:
```bash
docker compose down
```

## FastAPI Dashboard / FastAPI ダッシュボード
The project includes a FastAPI dashboard and a /health JSON endpoint for viewing system monitoring data through a browser or API client.

**日本語**:  
ブラウザやAPIクライアントからシステム監視データを確認できる FastAPI ダッシュボードと `/health` JSON エンドポイントが含まれています。

Local URLs / ローカルURL
| Page | URL |
| --- | --- |
| Dashboard | http://localhost:8000 |
| Health Endpoint | http://localhost:8000/health |
| Swagger UI | http://localhost:8000/docs |

## Tech Stack | 技術スタック 

- Python
- FastAPI
- Docker
- Docker Compose
- psutil
- colorama
- Slack Webhooks
- SMTP Email
- Git/GitHub