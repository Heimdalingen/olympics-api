"""Application configuration loaded from environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./olympics.db"
    initial_tokens: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
