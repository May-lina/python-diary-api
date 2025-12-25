from fastapi import FastAPI, Depends
from database import get_db,engine
from schemas import TaskCreate, TaskResponse
from sqlalchemy.orm import session
from models import Task, Base
Base.metadata.create_all(bind=engine)

app=FastAPI()

# @app.get("/")
# def get_home():
#     return{"welcome": "Maryam"}

@app.post("/tasks", response_model=TaskResponse)
def create_task(task_create:TaskCreate, db:session=Depends(get_db)):
    task=Task(title=task_create.title, content=task_create.content, description=task_create.description)
    # task=Task(**task_data.dict()) useful when you have many fields

    db.add(task)
    db.commit()
    db.refresh(task)
    return task
