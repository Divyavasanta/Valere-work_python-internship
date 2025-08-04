# main.py

from fastapi import FastAPI
from enum import Enum
from database import models
from database.db import engine
from routers import users, posts
from auth import router as auth_router # <-- Import the new auth router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="My Merged API",
    description="This API combines database operations with JWT authentication and RBAC.",
    version="1.0.0",
)

# --- Include Routers ---
# Include the new authentication router
app.include_router(
    auth_router,
    # No prefix needed here as it's defined in auth.py
)

# Include your existing routers
app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)
app.include_router(
    posts.router,
    prefix="/posts",
    tags=["Posts"],
)


# --- Public Endpoints (No login required) ---
class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    chinese = "chinese"

food_items = {
    'indian': ['biryani', 'paneer', 'dal'],
    'italian': ['pizza', 'pasta', 'lasagna'],
    'chinese': ['noodles', 'spring rolls', 'dumplings'],
    'american': ['burger', 'hot dog', 'fries']
}

@app.get("/", tags=["Public"])
def read_root():
    return {"message": "Welcome to the API!"}

@app.get("/get_items/{cuisine}", tags=["Public"])
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)