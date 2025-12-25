from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    content:str

class TaskResponse(BaseModel):
    id:int
    description:Optional[str]=None
    created_at:datetime
    content:str

class config:
    orm_mode=True        
