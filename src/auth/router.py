from fastapi import APIRouter

from src.auth.schemas import Token, Login


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/login/")
async def login(
    auth: Login,
) -> Token:
    return Token(
        type="Bearer",
        access_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
    )