# CoGym Production Backend

A high-performance, asynchronous FastAPI blueprint featuring RBAC, Celery workers, and Nginx orchestration.

## 🚀 Tech Stack
- **FastAPI** (Python 3.12, Async/Await)
- **PostgreSQL** (Database) + **Alembic** (Migrations)
- **Redis** (Message Broker) + **Celery** (Background Tasks)
- **Gunicorn** + **Uvicorn** (Production Servers)
- **Nginx** (Reverse Proxy)
- **OpenAI SDK** (AI Intelligence)

## 🛠 Local Setup (Mac/Linux)

1. **Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.local .env
   
```
export PYTHONPATH=$PYTHONPATH:.
python -m alembic upgrade head
```

### Common Commands

#### Environment Setup
```commandline
# Create the tables
docker-compose exec web alembic upgrade head

# Populate initial data (Admin user, S3 buckets, etc.)
docker-compose exec web python -m app.db.seeders.base
```

#### Initialize Infra
```commandline
docker-compose up -d --build
```

#### Database Setup
```commandline
# Create the tables
docker-compose exec web alembic upgrade head

# Populate initial data (Admin user, S3 buckets, etc.)
docker-compose exec web python -m app.db.seeders.base
```

```commandline
Start all services	docker-compose up -d
Stop all services	docker-compose stop
View all logs	docker-compose logs -f
Check DB tables	docker-compose exec db psql -U postgres -d dockert -c "\dt"
Generate Migration	docker-compose exec web alembic revision --autogenerate -m "msg"
```

### 📡 Running & Testing APIs

1. Interactive Documentation (Recommended)
FastAPI automatically generates an interactive UI.

- Swagger UI: http://localhost/api/docs

2. Curl Command
```commandline
curl -X 'POST' \
  'http://localhost/api/v1/auth/register' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@test.com",
  "password": "password123"
}'
```

#### Admin 
```commandline
creating admin user
docker exec -it cogym_web_1 python -m app.cli admin@example.com pass123
naviagte to http://localhost/admin
```