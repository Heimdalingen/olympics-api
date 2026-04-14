"""Managin users"""
from uuid import uuid4
from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User 
from app.utils.auth import hash_password

def get_user(db: Session, user_id: str):
    """Get a User by its ID"""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """Gets a user by its Mail"""
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    """Gets all the users"""
    return db.query(User).all()

def create_user(db: Session, email: str, password: str, initial_tokens: int):
    """Create and save a new user."""
    user = User(
        id=str(uuid4()),
        email=email,
        hashed_password=hash_password(password),
        tokens=initial_tokens
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user    

def update_user(db: Session, user_id: str, email: Optional[str], password: Optional[str]):
    """Updates the use's email and/or password"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user: 
        return None
    if email is not None:
        user.email = email
    if password is not None:
        user.hashed_password = hash_password(password)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str):
    """Deletes a selected ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user: 
        return None
    db.delete(user)
    db.commit()
