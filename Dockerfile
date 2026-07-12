# EN: Python base image
# JP: Python ベースイメージ
# KR: Python 기본 이미지

FROM python:3.11-slim


# EN: Set working directory
# JP: 作業ディレクトリ設定
# KR: 작업 디렉토리 설정

WORKDIR /app


# EN: Copy requirements file
# JP: requirementsファイルコピー
# KR: requirements 파일 복사

COPY requirements.txt .


# EN: Install dependencies
# JP: 依存関係インストール
# KR: 의존성 설치

RUN pip install --no-cache-dir -r requirements.txt


# EN: Copy project files
# JP: プロジェクトファイルコピー
# KR: 프로젝트 파일 복사

COPY . .


# EN: Expose FastAPI port
# JP: FastAPI のポートを公開
# KR: FastAPI 포트 공개

EXPOSE 8000


# EN: Run the health API service
# JP: ヘルスチェック API サービスを実行
# KR: 헬스체크 API 서비스를 실행

CMD ["python", "-m", "uvicorn", "health_api:app", "--host", "0.0.0.0", "--port", "8000"]