"""Schemas for user configuration"""
from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: Optional[str]
    password: Optional[str]


class UserUpdate(BaseModel):
    email: Optional[str]
    password: Optional[str]


class UserOut(BaseModel):
    id: str
    email: str
    tokens: int

    class Config:
        from_attributes = True


class TokenAdd(BaseModel):
    user_id: str
    amount: int
