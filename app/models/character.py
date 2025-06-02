from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from beanie import Document

class CharacterBase(BaseModel):
    name: str
    class_: str
    race: str
    gender: str
    age: str
    height: str
    weight: str
    eye_color: str
    skin_color: str
    hair_color: str
    description: str
    allies: str
    notes: str
    traits: str
    history: str
    equipment: str

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    class_: Optional[str] = None
    race: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    eye_color: Optional[str] = None
    skin_color: Optional[str] = None
    hair_color: Optional[str] = None
    description: Optional[str] = None
    allies: Optional[str] = None
    notes: Optional[str] = None
    traits: Optional[str] = None
    history: Optional[str] = None
    equipment: Optional[str] = None

class Character(Document, CharacterBase):
    owner_id: str
    created_at: datetime
    updated_at: datetime
    
    class Settings:
        name = "characters"
        
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Aragorn",
                "class_": "Guerreiro",
                "race": "Humano",
                "gender": "Masculino",
                "age": "87",
                "height": "1.98",
                "weight": "95",
                "eye_color": "Cinza",
                "skin_color": "Branco",
                "hair_color": "Preto",
                "description": "Um rei disfarçado que luta para proteger seus amigos.",
                "allies": "Gandalf, Legolas, Gimli",
                "notes": "Possui uma espada chamada Andúril.",
                "traits": "Corajoso, Líder",
                "history": "Filho de Arathorn, herdeiro do trono de Gondor.",
                "equipment": "Espada Andúril, Capa, Anel",
                "owner_id": "507f1f77bcf86cd799439011",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-01T00:00:00"
            }
        }