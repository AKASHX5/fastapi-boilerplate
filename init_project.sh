#!/bin/bash

# Exit on error
set -e

echo "🚀 Initializing your new FastAPI Boilerplate..."

# 1. Ask for Project Name
read -p "Enter Project Name (default: my_fastapi_app): " PROJECT_NAME
PROJECT_NAME=${PROJECT_NAME:-my_fastapi_app}

# 2. Ask for Database Name
read -p "Enter Database Name (default: ${PROJECT_NAME}_db): " DB_NAME
DB_NAME=${DB_NAME:-${PROJECT_NAME}_db}

# 3. Generate a random Secret Key
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')

# 4. Create .env from template
if [ -f .env ]; then
    echo "⚠️  .env already exists. Skipping creation."
else
    echo "📝 Creating .env file..."
    cat <<EOF > .env
# --- Project Meta ---
PROJECT_NAME=${PROJECT_NAME}
DEBUG=true
API_PORT=8000

# --- Security ---
SECRET_KEY=${SECRET_KEY}
OPENAI_API_KEY=your_openai_key_here

# --- Database ---
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=${DB_NAME}
DB_HOST=db
DB_PORT=5432

# Construction of the URL for SQLAlchemy/Alembic
DATABASE_URL=postgresql+asyncpg://\${DB_USER}:\${DB_PASSWORD}@\${DB_HOST}:\${DB_PORT}/\${DB_NAME}

# --- Infrastructure ---
S3_BUCKET_NAME=${PROJECT_NAME}-assets
S3_ENDPOINT_URL=http://localhost:4566
REDIS_URL=redis://redis:6379/0
EOF
fi

# 5. Final Instructions
echo "------------------------------------------------"
echo "✅ Initialization complete for project: ${PROJECT_NAME}"
echo "------------------------------------------------"
echo "Next steps:"
echo "  1. Run 'docker-compose up -d --build'"
echo "  2. Run 'docker-compose exec web alembic upgrade head'"
echo "  1. Run 'docker exec -it cogym_web_1 python -m app.cli admin@example.com pass123'"
echo "  3. Open http://localhost:8000/api/docs"
echo "------------------------------------------------"