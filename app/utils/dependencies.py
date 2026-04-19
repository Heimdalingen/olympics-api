"""Handles all the dependencies for the assignment-1"""
from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User


def consume_token(user_id: str, db: Session = Depends(get_db)):
    """Deduct one token from the user or raise an error."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.tokens <= 0:
        raise HTTPException(status_code=402, detail="Insufficient tokens")
    user.tokens -= 1
    db.commit()
