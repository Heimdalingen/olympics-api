"""User database model."""
from app.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    """Database model for a user."""
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    tokens = Column(Integer, nullable=False, default=0)
