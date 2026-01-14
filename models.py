from sqlalchemy import Integer, Column,String,Text, Boolean,ForeignKey,DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__="tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tasks")
 

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True,index=True)
    username = Column(String, unique=True)
    password = Column(String) #or Text
    tasks = relationship("Task", back_populates="owner")#owner point back to the user
    bins = relationship("TaskBin", back_populates="owner")


class TaskBin(Base):
    __tablename__ = "task_bins"

    id = Column(Integer, primary_key=True, index=True)
    original_task_id = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="bins")





