"""Handels Olympic data query service."""
from sqlalchemy.orm import Session
from typing import Optional
from app.models.olympic import OlympicEvent
from app.schemas.olympic import OlympicEventCreate


def get_athlete(db: Session, athlete_id: int, limit: int = 100):
    """Gets athletes and filters it"""
    return db.query(OlympicEvent).filter(OlympicEvent.
                                         athlete_id == athlete_id).limit(limit).all()


def get_country(db: Session, noc: str, limit: int = 100):
    """Gets country and filters by Event"""
    return db.query(OlympicEvent).filter(OlympicEvent.noc == noc).limit(limit).all()


def get_sport(db: Session,
              sport: str,
              country: Optional[str],
              year: Optional[int],
              medal: Optional[str],
              limit: int = 100):
    """Gets the sport"""
    query = db.query(OlympicEvent).filter(OlympicEvent.sport == sport)
    if country:
        query = query.filter(OlympicEvent.noc == country.upper())
    if year:
        query = query.filter(OlympicEvent.year == year)
    if medal:
        query = query.filter(OlympicEvent.medal == medal.capitalize())
    return query.limit(limit).all()


def create_event(db: Session, event_data: OlympicEventCreate):
    """Creates a new Olympic event record."""
    event = OlympicEvent(**event_data.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
