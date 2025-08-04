# database/schemas.py
from pydantic import BaseModel, ConfigDict
from typing import List

# --- Post Schemas ---
class PostBase(BaseModel):
    title: str
    content: str | None = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    
    model_config = ConfigDict(from_attributes=True)

# --- User Schemas (Updated) ---
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []  # Add this line to show posts
    
    model_config = ConfigDict(from_attributes=True)