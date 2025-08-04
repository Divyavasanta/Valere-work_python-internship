from sqlalchemy.orm import Session, joinedload
from . import models, schemas


# --- READ Operations ---

def get_user(db: Session, user_id: int):
    # THIS IS THE CORRECTED FUNCTION
    # We add .options(joinedload(models.User.posts)) to tell SQLAlchemy
    # to fetch the related posts in the same query.
    return db.query(models.User).options(joinedload(models.User.posts)).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    # We can also add eager loading here if we want to see all posts for all users
    return db.query(models.User).options(joinedload(models.User.posts)).offset(skip).limit(limit).all()

# --- CREATE Operation ---

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.model_dump(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post