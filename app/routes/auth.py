from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..services.auth import AuthService
from ..models.user import UserCreate
from ..utils.security import get_current_user
from ..models.user import UserInDB

router = APIRouter()

@router.post("/register", response_model=UserInDB)
async def register(user_data: UserCreate):
    return await AuthService.register_user(user_data)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await AuthService.login_user(form_data.username, form_data.password)

@router.get("/me", response_model=UserInDB)
async def get_current_user_data(current_user: UserInDB = Depends(get_current_user)):
    return current_user