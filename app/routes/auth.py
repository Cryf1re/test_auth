from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from authx import AuthX, AuthXConfig
from app.config import get_settings
from app.database import get_async_session
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.services.auth_service import hash_password, authenticate_user, get_user_by_username

settings = get_settings()

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY=settings.SECRET_KEY,
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    existing = await get_user_by_username(session, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=await hash_password(user.password)
    )
    session.add(new_user)
    await session.commit()
    return auth.create_access_token(data={"sub": user.username})

@router.post("/login")
async def login(user: UserLogin, session: AsyncSession = Depends(get_async_session)):
    db_user = await authenticate_user(session, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth.create_access_token(data={"sub": db_user.username})