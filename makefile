.PHONY: init up down build rebuild reset logs shell migrate worker flower ps

COMPOSE=docker-compose
PROJECT?=default
# -----------------------------
# INIT
# -----------------------------
init:
	@chmod +x scripts/init_env.sh
	@./scripts/init_env.sh

# -----------------------------
# DOCKER LIFECYCLE
# -----------------------------

up:
	@$(COMPOSE) -p $(PROJECT) up -d

down:
	@$(COMPOSE) -p $(PROJECT) down

reset:
	@$(COMPOSE) -p $(PROJECT) down -v --remove-orphans

logs:
	@$(COMPOSE) -p $(PROJECT) logs -f

ps:
	@$(COMPOSE) -p $(PROJECT) ps

# -----------------------------
# DATABASE
# -----------------------------
migrate:
	@$(COMPOSE) exec web alembic upgrade head

makemigration:
	@$(COMPOSE) exec web alembic revision --autogenerate -m "auto"

# -----------------------------
# SHELL ACCESS
# -----------------------------
shell:
	@$(COMPOSE) exec web bash

dbshell:
	@$(COMPOSE) exec db psql -U postgres

# -----------------------------
# CELERY
# -----------------------------
worker:
	@$(COMPOSE) logs -f worker

# -----------------------------
# OPTIONAL (if you add flower)
# -----------------------------
flower:
	@$(COMPOSE) up -d flower