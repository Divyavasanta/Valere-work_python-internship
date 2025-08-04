# schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class ScrapeTaskCreate(BaseModel):
    """Schema for creating a new scrape task."""
    url: str = Field(..., example="https://www.google.com")

class ScrapeTask(BaseModel):
    """Schema representing a single scrape task in our database."""
    task_id: uuid.UUID
    status: str
    url: str
    results: Optional[List[str]] = None # Results will be a list of headlines

    class Config:
        from_attributes= True