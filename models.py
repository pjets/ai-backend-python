from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    fullname: str
    phone_number: str
    birthday: date


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: str
    fullname: str
    phone_number: str
    birthday: date
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
