from datetime import datetime
from typing import List, Optional
from ..models.character import Character, CharacterCreate, CharacterUpdate
from ..database.mongodb import db
from ..utils.logger import logger

class CharacterService:
    @staticmethod
    async def list_characters(owner_id: str) -> List[Character]:
        characters = await Character.find({"owner_id": owner_id}).to_list()
        logger.info(f"Retrieved {len(characters)} characters for user {owner_id}")
        return characters

    @staticmethod
    async def create_character(owner_id: str, character_data: CharacterCreate) -> Character:
        now = datetime.utcnow()
        character = Character(
            **character_data.dict(),
            owner_id=owner_id,
            created_at=now,
            updated_at=now
        )
        await character.insert()
        logger.info(f"Character created: {character.name} for user {owner_id}")
        return character

    @staticmethod
    async def get_character(owner_id: str, character_id: str) -> Optional[Character]:
        character = await Character.find_one({"_id": character_id, "owner_id": owner_id})
        if character:
            logger.info(f"Character retrieved: {character_id} for user {owner_id}")
        else:
            logger.warning(f"Character not found: {character_id} for user {owner_id}")
        return character

    @staticmethod
    async def update_character(
        owner_id: str, 
        character_id: str, 
        character_data: CharacterUpdate
    ) -> Optional[Character]:
        character = await Character.find_one({"_id": character_id, "owner_id": owner_id})
        if not character:
            return None
            
        update_data = character_data.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        
        await character.update({"$set": update_data})
        updated_character = await Character.find_one({"_id": character_id})
        
        logger.info(f"Character updated: {character_id} for user {owner_id}")
        return updated_character

    @staticmethod
    async def patch_character(
        owner_id: str, 
        character_id: str, 
        character_data: CharacterUpdate
    ) -> Optional[Character]:
        # Same as update for this implementation
        return await CharacterService.update_character(owner_id, character_id, character_data)

    @staticmethod
    async def delete_character(owner_id: str, character_id: str) -> bool:
        character = await Character.find_one({"_id": character_id, "owner_id": owner_id})
        if not character:
            return False
            
        await character.delete()
        logger.info(f"Character deleted: {character_id} by user {owner_id}")
        return True

    @staticmethod
    async def generate_text(prompt: str) -> dict:
        # This is a mock implementation similar to the frontend handler
        name_match = prompt.split("Name:")[1].split("\n")[0].strip() if "Name:" in prompt else "Personagem Desconhecido"
        fake_backstory = f"[História dramática sobre {name_match}]"
        
        logger.info(f"Text generated for prompt: {prompt[:50]}...")
        return {"Generated Text": fake_backstory}