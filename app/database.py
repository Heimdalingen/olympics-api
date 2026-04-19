"""Database engine, session factory, and base model setup."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings


engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    """Yield a database session and close it once its done."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
