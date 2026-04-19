"""Router for country endpoints."""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import query_services
from app.utils.dependencies import consume_token
from app.utils.responses import format_response

router = APIRouter(prefix="/v1/country", tags=["countries"])


@router.get("/{noc}")
def get_country(noc: str, user_id: str, request: Request, db: Session = Depends(get_db), limit: int = 100):
    """Return all Olympic events for a given country NOC code."""
    consume_token(user_id, db)
    events = query_services.get_country(db, noc, limit)
    if not events:
        raise HTTPException(status_code=404, detail="Country not found")
    return format_response(events, request.headers.get("accept", ""))
