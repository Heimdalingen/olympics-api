"""Endpoint for Tokens."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import TokenAdd
from app.services import token_services

router = APIRouter(prefix="/v1/tokens", tags=["tokens"])


@router.post("")
def add_tokens(body: TokenAdd, db: Session = Depends(get_db)):
    """Add tokens to a user's balance."""
    tokens = token_services.add_tokens(db, body.user_id, body.amount)
    if not tokens:
        raise HTTPException(status_code=404, detail="User banished, forgotten")
    return tokens
