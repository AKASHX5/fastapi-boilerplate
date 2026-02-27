#!/bin/bash
set -e

echo "🚀 Initializing FastAPI project..."

read -p "Enter Project Name (default: my_fastapi_app): " PROJECT_NAME
PROJECT_NAME=${PROJECT_NAME}
COMPOSE_PROJECT_NAME=${PROJECT_NAME}
if [[ ! "$PROJECT_NAME" =~ ^[a-zA-Z0-9][a-zA-Z0-9_.-]+$ ]]; then
  echo "❌ Invalid project name. Must match [a-zA-Z0-9][a-zA-Z0-9_.-]"
  exit 1
fi

read -p "Enter Database Name (default: ${PROJECT_NAME}_db): " DB_NAME
DB_NAME=${DB_NAME:-${PROJECT_NAME}_db}

SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')

cat > .env <<EOF
PROJECT_NAME=${PROJECT_NAME}
DEBUG=true
API_PORT=8000

SECRET_KEY=${SECRET_KEY}

DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=${DB_NAME}
DB_HOST=db
DB_PORT=5432

DATABASE_URL=postgresql+asyncpg://\${DB_USER}:\${DB_PASSWORD}@\${DB_HOST}:\${DB_PORT}/\${DB_NAME}

REDIS_URL=redis://redis:6379/0

S3_BUCKET_NAME=${PROJECT_NAME}-assets
S3_ENDPOINT_URL=http://localstack:4566
EOF

echo "✅ .env created successfully"