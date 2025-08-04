from fastapi import APIRouter, Depends
from authx import AuthX, AuthXConfig
from app.config import get_settings

settings = get_settings()
config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY=settings.SECRET_KEY,
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

router = APIRouter()

@router.get("/me")
async def get_me(user=Depends(auth.get_current_user)):
    return {"username": user["sub"]}