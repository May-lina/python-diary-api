from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    content: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    description: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    content: str
    description: Optional[str]
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class TaskBinResponse(BaseModel):
    id: int
    original_task_id: int
    title: str
    content: str | None
    description: str | None
    owner_id: int
    created_at: datetime
    deleted_at: datetime

    class Config:
        from_attributes = True

