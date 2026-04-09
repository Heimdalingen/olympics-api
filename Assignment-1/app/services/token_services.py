"""Handles Tokens"""
from sqlalchemy.orm import Session
from app.models.user import User

def add_tokens(db: Session, user_id: str, amount: int):
    """Adds tokens"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.tokens += amount
    db.commit()
    db.refresh(user)
    return user