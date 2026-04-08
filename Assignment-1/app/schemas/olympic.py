"""Olympic Schemas"""
from pydantic import BaseModel

class OlympicEventOut(BaseModel):
    id: int
    athlete_id: int | None
    name: str | None
    sex: str | None
    age: int| None
    height: int | None
    weight: int | None
    team: str | None
    noc: str | None
    year: int | None
    season: str | None
    city: str | None
    sport: str | None
    event: str | None
    medal: str | None

    class Config:
        from_attributes = True

class OlympicEventCreate(BaseModel):
    name: str
    sex: str
    team: str
    noc: str
    year: int
    season: str
    city: str
    sport: str
    event: str
    athlete_id: int | None = None
    age: int | None = None
    weight: int | None = None
    medal: str | None = None

