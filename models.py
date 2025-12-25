from sqlalchemy import Integer, Column,String,Text, Boolean,DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(200), nullable=False)
    content=Column(Text, nullable=True)
    description=Column(Text, nullable=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__="user.db"
    id=Column(int, primary_key=True)
    email=Column(str, unique_key=True)
    username=Column(str, unique_key=True)
    password=Column(str)