"""Olympic event database model."""
from app.database import Base
from sqlalchemy import Column, String, Integer


class OlympicEvent(Base):
    """Database model for an Olympic event record."""
    __tablename__ = "olympic_events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(Integer, nullable=True)
    name = Column(String)
    sex = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    team = Column(String)
    noc = Column(String, nullable=False)
    year = Column(Integer)
    season = Column(String)
    city = Column(String)
    sport = Column(String)
    event = Column(String)
    medal = Column(String, nullable=True)
