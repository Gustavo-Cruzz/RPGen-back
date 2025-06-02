from fastapi import APIRouter, Depends, HTTPException
from ..services.ai_service import AIService
from ..utils.security import get_current_user
from ..models.user import UserInDB

router = APIRouter()
ai_service = AIService()

@router.post("/gerar-texto")
async def generate_text(
    prompt: str,
    current_user: UserInDB = Depends(get_current_user)
):
    try:
        generated_text = ai_service.generate_text(prompt)
        if not generated_text:
            raise HTTPException(status_code=500, detail="Failed to generate text")
        return {"Generated Text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/gerar-imagem")
async def generate_image(
    prompt: str,
    current_user: UserInDB = Depends(get_current_user)
):
    try:
        image_data = ai_service.generate_image(prompt)
        if not image_data:
            raise HTTPException(status_code=500, detail="Failed to generate image")
        return {"image_data": image_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))