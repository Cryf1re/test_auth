from fastapi import APIRouter

from app.routes import (
    auth,
    protected,
)

router = APIRouter()
router.include_router(auth.router)
router.include_router(protected.router)