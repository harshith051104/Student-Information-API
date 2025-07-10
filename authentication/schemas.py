# authentication/schemas.py
#
# Pydantic models (schemas) for the authentication module.

from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
