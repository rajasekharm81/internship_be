import os
from datetime import datetime
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from starlette import status
from constants import Secret
from shared.database.schemas import CurrentUser
from passlib.context import CryptContext

oauth2_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_current_user(token=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = None
    try:
        payload = jwt.decode(token.credentials, Secret.JWT, algorithms=[Secret.ALGORITHM])
        if datetime.fromtimestamp(payload.get('exp')) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = payload

    except jwt.exceptions.PyJWTError:
        raise credentials_exception

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: CurrentUser = Depends(get_current_user)):
    if current_user['is_active'] == 0:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

