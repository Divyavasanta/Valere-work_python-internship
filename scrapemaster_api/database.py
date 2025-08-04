# database.py
import uuid
from typing import Dict
from schemas import ScrapeTask

# This dictionary will act as our in-memory database.
db: Dict[uuid.UUID, ScrapeTask] = {}

# NEW FUNCTION
def create_scrape_task(url: str) -> ScrapeTask:
    """Creates a new scrape task entry in the database."""
    new_task = ScrapeTask(
        task_id=uuid.uuid4(),
        status="in_progress",
        url=url,
        results=None,
    )
    db[new_task.task_id] = new_task
    return new_task