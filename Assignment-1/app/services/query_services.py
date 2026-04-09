"""Handels Olympic data query service."""
from sqlalchemy.orm import Session
from app.models.olympic import OlympicEvent
from app.schemas.olympic import OlympicEventCreate


def get_athlete(db: Session, atlhete_id: int):
    """Gets athletes and filters it"""
    return db.query(OlympicEvent).filter(OlympicEvent.athlete_id == atlhete_id).all()


def get_country(db: Session, noc: str):
    """Gets country and filters by Event"""
    return db.query(OlympicEvent).filter(OlympicEvent.noc == noc).all()


def get_sport(db: Session, sport: str, country: str | None, year: int | None, medal: str | None):
    """Gets the sport"""
    query = db.query(OlympicEvent).filter(OlympicEvent.sport == sport)
    if country:
        query = query.filter(OlympicEvent.noc == country.upper())
    if year:
        query = query.filter(OlympicEvent.year == year)
    if medal:
        query = query.filter(OlympicEvent.medal == medal.capitalize())
    return query.all()


def create_event(db: Session, event_data: OlympicEventCreate):
    """Creates a new Olympic event record."""
    event = OlympicEvent(**event_data.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event