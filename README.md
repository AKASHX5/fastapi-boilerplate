# FastApi Boilerplate Production Backend

A production-ready FastAPI backend boilerplate designed for real-world systems.
Includes async architecture, RBAC-ready auth, background workers, and Docker-based infrastructure with clean project initialization.

##Features
- Fully async FastAPI architecture (Python 3.12)

- PostgreSQL with Alembic migrations

- Redis + Celery for background jobs

- Docker Compose–based local orchestration

- LocalStack for S3-compatible development

- Makefile-driven developer workflow

## 🚀 Tech Stack
- **FastAPI** (Python 3.12, Async/Await)
- **PostgreSQL** (Database) + **Alembic** (Migrations)
- **Redis** (Message Broker) + **Celery** (Background Tasks)
- **Gunicorn** + **Uvicorn** (Production Servers)
- **Nginx** (Reverse Proxy)
- **OpenAI SDK** (AI Intelligence)

## 🛠 Quick Setup (Mac/Linux)

   ```bash
git clone <repo-url>
cd fastapi-boilerplate   
```

#### Initialize Infra
```commandline
make up        # Start all services
make down      # Stop all services
make reset     # Destroy containers, volumes, networks
make ps        # List running containers
make logs      # Follow logs
```

#### Database Setup
```commandline
make migrate        # Apply migrations
make makemigration # Generate new migration
make dbshell       # Open PostgreSQL shell

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
docker-compose exec web python -m app.cli admin@example.com pass123
naviagte to http://localhost/admin
```