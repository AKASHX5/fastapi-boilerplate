from app.worker.celery_app import celery
import time


@celery.task(bind=True)
def example_task(self, seconds: int):
    for i in range(seconds):
        time.sleep(1)
        self.update_state(state="PROGRESS", meta={"current": i + 1})
    return {"status": "completed"}
