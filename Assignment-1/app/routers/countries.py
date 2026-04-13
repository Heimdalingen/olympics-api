from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import query_services
from app.utils.dependencies import consume_token

router = APIRouter(prefix="/v1/country", tags=["countries"])

@router.get("/{noc}")
def get_country(noc: str, user_id: str, db: Session = Depends(get_db)):
    consume_token(user_id, db)
    events = query_services.get_country(db, noc)
    if not events:
        raise HTTPException(status_code=404, detail="Country not found")
    return events

    
