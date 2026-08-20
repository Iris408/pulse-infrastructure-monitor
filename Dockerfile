# EN: Python base image
# JP: Python ベースイメージ

FROM python:3.11-slim

# EN: Prevent Python from writing .pyc files and buffer-free logs.
# JP: .pycファイルの生成を防ぎ、ログを即時出力します。
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# EN: Set working directory
# JP: 作業ディレクトリ設定

WORKDIR /app


# EN: Copy requirements file
# JP: requirementsファイルコピー

COPY requirements.txt .


# EN: Install dependencies
# JP: 依存関係インストール

RUN pip install --no-cache-dir -r requirements.txt


# EN: Copy project files
# JP: プロジェクトファイルコピー

COPY . .


# EN: Expose FastAPI port
# JP: FastAPI のポートを公開

EXPOSE 8000


# EN: Run the health API service
# JP: ヘルスチェック API サービスを実行

CMD ["python", "-m", "uvicorn", "app.api.health:app", "--host", "0.0.0.0", "--port", "8000"]