run:
	uvicorn app.main:app --reload

test:
	pytest --cov=app --cov-report=term-missing

migrate:
	python -m alembic upgrade head

docker-build:
	docker-compose -f docker-compose.prod.yml up --build -d