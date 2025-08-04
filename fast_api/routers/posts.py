# Example for routers/posts.py

from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_active_user, require_role # <-- Import dependencies
from auth import User # Import the User model for type hinting
import random # <-- Import the random module to generate IDs

router = APIRouter()

# --- Example Endpoints ---

# 1. Anyone who is logged in can create a post.
@router.post("/create")
async def create_post(
    post_content: str,
    current_user: User = Depends(get_current_active_user)
):
    # In a real application, you would save the post to the database
    # and get the new post's ID from the database.
    # For this example, we'll just generate a random ID.
    new_post_id = random.randint(100, 1000)

    return {
        "message": "Post created successfully!",
        "post_id": new_post_id, # <-- ADDED: post_id is now in the response
        "owner": current_user.username,
        "content": post_content
    }

# 2. Only users with the "editor" role can edit a post.
@router.put("/edit/{post_id}")
async def edit_post(
    post_id: int,
    # This endpoint requires a logged-in user who is ALSO an editor
    current_user: User = Depends(require_role("editor"))
):
    return {
        "message": f"Post {post_id} has been edited by {current_user.username}",
        "status": "success"
    }

# 3. Only users with the "admin" role can delete a post.
@router.delete("/delete/{post_id}")
async def delete_post(
    post_id: int,
    # This endpoint requires a logged-in user who is ALSO an admin
    current_user: User = Depends(require_role("admin"))
):
    return {
        "message": f"Admin {current_user.username} has deleted post {post_id}",
        "status": "success"
    }