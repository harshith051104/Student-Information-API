# authentication/routes.py
#
# API endpoints (routes) for the authentication module.

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from config import settings
from database import user_collection
from . import schemas, utils

router = APIRouter()

@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: schemas.UserCreate):
    """Register a new user in the database."""
    db_user = utils.get_user(user_in.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = utils.get_password_hash(user_in.password)
    user_doc = user_in.model_dump()
    user_doc.pop("password")
    user_doc["hashed_password"] = hashed_password
    user_doc["disabled"] = False
    
    user_collection.insert_one(user_doc)
    return user_doc

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Authenticate user and return a JWT access token."""
    user = utils.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKENS_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: Annotated[schemas.User, Depends(utils.get_current_active_user)]):
    """Fetch the details of the currently authenticated user."""
    return current_user
