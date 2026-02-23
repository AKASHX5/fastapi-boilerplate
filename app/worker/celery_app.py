from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery(
    "ai_enrichment_worker",
    broker=REDIS_URL,
    backend=REDIS_URL,  # optional but useful for tracking results
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Optional: auto-discover tasks inside app.tasks
celery.autodiscover_tasks(["app"])
