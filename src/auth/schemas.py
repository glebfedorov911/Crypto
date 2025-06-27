from pydantic import BaseModel


class Token(BaseModel):
    type: str
    access_token: str

class Login(BaseModel):
    login: str
    password: str