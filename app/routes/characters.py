from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..models.character import Character, CharacterCreate, CharacterUpdate
from ..services.character import CharacterService
from ..utils.security import get_current_user
from ..models.user import UserInDB

router = APIRouter()

@router.get("/", response_model=List[Character])
async def list_characters(current_user: UserInDB = Depends(get_current_user)):
    return await CharacterService.list_characters(current_user.id)

@router.post("/", response_model=Character, status_code=status.HTTP_201_CREATED)
async def create_character(
    character_data: CharacterCreate,
    current_user: UserInDB = Depends(get_current_user)
):
    return await CharacterService.create_character(current_user.id, character_data)

@router.get("/{character_id}", response_model=Character)
async def get_character(
    character_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    character = await CharacterService.get_character(current_user.id, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.put("/{character_id}", response_model=Character)
async def update_character(
    character_id: str,
    character_data: CharacterUpdate,
    current_user: UserInDB = Depends(get_current_user)
):
    updated = await CharacterService.update_character(
        current_user.id, character_id, character_data
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Character not found")
    return updated

@router.patch("/{character_id}", response_model=Character)
async def patch_character(
    character_id: str,
    character_data: CharacterUpdate,
    current_user: UserInDB = Depends(get_current_user)
):
    updated = await CharacterService.patch_character(
        current_user.id, character_id, character_data
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Character not found")
    return updated

@router.delete("/{character_id}")
async def delete_character(
    character_id: str,
    current_user: UserInDB = Depends(get_current_user)
):
    deleted = await CharacterService.delete_character(current_user.id, character_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": f"Character {character_id} deleted successfully."}

@router.post("/api/gerar-texto")
async def generate_text(prompt: str, current_user: UserInDB = Depends(get_current_user)):
    return await CharacterService.generate_text(prompt)