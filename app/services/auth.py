from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from ..models.user import User, UserCreate, UserInDB
from ..database.mongodb import db
from ..config import settings
from ..utils.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    async def register_user(user_data: UserCreate) -> UserInDB:
        existing_user = await db.users.find_one({"$or": [{"username": user_data.username}, {"email": user_data.email}]})
        if existing_user:
            logger.warning(f"Attempt to register with existing username or email: {user_data.username}")
            raise ValueError("Username or email already exists")
        
        hashed_password = pwd_context.hash(user_data.password)
        now = datetime.utcnow()
        
        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            created_at=now,
            updated_at=now
        )
        
        await user.insert()
        logger.info(f"User registered successfully: {user_data.username}")
        return UserInDB(**user.dict())

    @staticmethod
    async def login_user(username: str, password: str) -> dict:
        user = await db.users.find_one({"username": username})
        if not user or not pwd_context.verify(password, user["hashed_password"]):
            logger.warning(f"Failed login attempt for username: {username}")
            raise ValueError("Invalid credentials")
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = AuthService.create_access_token(
            data={"sub": user["username"]}, expires_delta=access_token_expires
        )
        
        logger.info(f"User logged in successfully: {username}")
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "username": user["username"],
                "email": user["email"]
            }
        }

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_current_user_data(username: str) -> UserInDB:
        user = await db.users.find_one({"username": username})
        if not user:
            raise ValueError("User not found")
        return UserInDB(**user)