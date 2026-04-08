"""Schemas for user configuration"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None


class UserOut(BaseModel):
    id: str
    email: str
    tokens: int

    class Config:
        from_attributes = True


class TokenAdd(BaseModel):
    user_id: str
    amount: int
    