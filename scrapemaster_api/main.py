# main.py
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import scrape # Import the router we just created
from routers.scrape import TaskNotFoundException # Import our custom exception
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ScrapeMaster API",
    description="A simple API to scrape web content asynchronously.",
    version="1.0.0",
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "null"  # <-- THIS IS THE KEY FOR LOCAL FILE TESTING
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods, including OPTIONS
    allow_headers=["*"], # Allows all headers
)

# --- NEW: Custom Exception Handler ---
@app.exception_handler(TaskNotFoundException)
async def task_not_found_exception_handler(request: Request, exc: TaskNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"error": "Task not found", "task_id": str(exc.task_id)},
    )

# --- Include Routers ---
# This is where we "plug in" our mini-application from routers/scrape.py
app.include_router(
    scrape.router,
    prefix="/scrape", # Add a URL prefix for all endpoints in this router
    tags=["Scraping"], # Group these endpoints in the API docs
)


@app.get("/", tags=["Root"])
async def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the ScrapeMaster API!"}