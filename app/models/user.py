from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from beanie import Document, Indexed

class UserBase(BaseModel):
    username: str
    email: EmailStr
    
class UserCreate(UserBase):
    password: str
    
class UserInDB(UserBase):
    id: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime

class User(Document, UserInDB):
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    
    class Settings:
        name = "users"
        
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "hashed_password": "hashedpassword123",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-01T00:00:00"
            }
        }