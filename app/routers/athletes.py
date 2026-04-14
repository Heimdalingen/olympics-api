from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import query_services
from app.utils.dependencies import consume_token

router = APIRouter(prefix="/v1/athlete", tags=["athletes"])

@router.get("/{athlete_id}")
def get_athlete(athlete_id: int, user_id: str, db: Session = Depends(get_db)):
    consume_token(user_id, db)
    events = query_services.get_athlete(db, athlete_id)
    if not events:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return events

    
