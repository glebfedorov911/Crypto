from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.application.router import router as application_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(application_router)