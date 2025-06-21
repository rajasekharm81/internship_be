from typing import Optional, List
from pydantic import BaseModel

class CurrentUser(BaseModel):
    username:str
    user_id:str
    is_active:int
    
class UserLoginRequest(BaseModel):
    username: str
    password: str

class CreateUserRequest(BaseModel):
    name:str
    username: str
    password: str