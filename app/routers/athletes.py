"""Router for athlete endpoints."""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import query_services
from app.utils.dependencies import consume_token
from app.utils.responses import format_response

router = APIRouter(prefix="/v1/athlete", tags=["athletes"])


@router.get("/{athlete_id}")
def get_athlete(athlete_id: int, user_id: str, request: Request, db: Session = Depends(get_db)):
    """Return all Olympic events for a given athlete."""
    consume_token(user_id, db)
    events = query_services.get_athlete(db, athlete_id)
    if not events:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return format_response(events, request.headers.get("accept", ""))
