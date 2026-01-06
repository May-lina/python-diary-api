from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    content:str
    owner_id:int

class TaskResponse(BaseModel):
    id:int
    description:Optional[str]=None
    created_at:datetime
    content:str
    owner_id:int

class UserCreate(BaseModel):
    email:str
    username:str
    password:str

class UserResponse(BaseModel):
    email:str
    username:str

class TaskUpdate(BaseModel):
    title:str | None = None
    content:str | None = None   
    description:str | None = None 


class LoginRequest(BaseModel):
    username: str
    password: str

class config:
    orm_mode=True        
