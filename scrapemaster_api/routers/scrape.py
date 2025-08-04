# routers/scrape.py
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
import uuid
import httpx
from bs4 import BeautifulSoup

from schemas import ScrapeTaskCreate, ScrapeTask
from database import db, create_scrape_task

# Create a new router instance
router = APIRouter()

class TaskNotFoundException(Exception):
    def __init__(self, task_id: uuid.UUID):
        self.task_id = task_id



def scrape_website_headlines(task_id: uuid.UUID, url: str):
    """
    The actual scraping logic that runs in the background.
    It scrapes H1 and H2 tags from the given URL.
    """
    print(f"Scraping started for task {task_id} on URL: {url}")
    try:
        # Make an HTTP request to the URL
        response = httpx.get(url, follow_redirects=True, timeout=20.0)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all h1 and h2 tags and extract their text
        headlines = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2'])]
        
        # Update the task in our "database"
        db[task_id].status = "complete"
        db[task_id].results = headlines
        print(f"Scraping finished for task {task_id}. Found {len(headlines)} headlines.")

    except Exception as e:
        print(f"Scraping failed for task {task_id}: {e}")
        db[task_id].status = "failed"


@router.post("/", response_model=ScrapeTask, status_code=202)
async def create_scraping_task(
    task_in: ScrapeTaskCreate, background_tasks: BackgroundTasks
):
    """
    Create a new scraping task.
    The scraping itself is run as a background task.
    """
    # Create an entry in our database
    new_task = create_scrape_task(url=task_in.url)

    # Add the slow scraping function to run in the background
    background_tasks.add_task(scrape_website_headlines, new_task.task_id, new_task.url)
    
    # Return the task details to the client immediately
    return new_task

# NEW: Endpoint to retrieve task status and results
@router.get("/{task_id}", response_model=ScrapeTask)
async def get_scraping_task(task_id: uuid.UUID):
    """
    Retrieves the status and results of a scraping task.
    """
    task = db.get(task_id)
    if not task:
        # If task is not found, raise our custom exception
        raise TaskNotFoundException(task_id=task_id)
    return task

# routers/scrape.py

# ... (all your existing imports and code) ...

# NEW: Endpoint to delete a task
@router.delete("/{task_id}", status_code=200)
async def delete_scraping_task(task_id: uuid.UUID):
    """
    Deletes a scraping task and its results.
    """
    task = db.get(task_id)
    if not task:
        # If task is not found, raise our custom exception
        raise TaskNotFoundException(task_id=task_id)
    
    # Delete the task from our "database"
    del db[task_id]
    
    return {"message": "Task deleted successfully", "task_id": task_id}