from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import query_services
from app.utils.dependencies import consume_token
from typing import Optional

router = APIRouter(prefix="/v1/sport", tags=["sports"])

@router.get("/{sport}")
def get_sport(sport: str, user_id: str, db: Session = Depends(get_db),
    country: Optional[str] = None,
    year: Optional[int] = None,
    medal: Optional[str] = None):
    consume_token(user_id, db)
    events = query_services.get_sport(db, sport, country, year, medal)
    if not events:
        raise HTTPException(status_code=404, detail="sport not found")
    return events

