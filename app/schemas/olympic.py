"""Olympic Schemas"""
from typing import Optional
from pydantic import BaseModel


class OlympicEventOut(BaseModel):
    """Schema for returning an Olympic event."""
    id: int
    athlete_id: Optional[int] = None
    name: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    team: Optional[str] = None
    noc: Optional[str] = None
    year: Optional[int] = None
    season: Optional[str] = None
    city: Optional[str] = None
    sport: Optional[str] = None
    event: Optional[str] = None
    medal: Optional[str] = None

    class Config:
        from_attributes = True


class OlympicEventCreate(BaseModel):
    """Schema for creating a new Olympic event."""
    name: str
    sex: str
    team: str
    height: Optional[int] = None
    noc: str
    year: int
    season: str
    city: str
    sport: str
    event: str
    athlete_id: Optional[int] = None
    age: Optional[int] = None
    weight: Optional[int] = None
    medal: Optional[str] = None
