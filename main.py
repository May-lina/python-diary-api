from fastapi import FastAPI, Depends
from database import get_db,engine
from schemas import TaskCreate, TaskResponse, UserCreate, UserResponse, TaskUpdate
from sqlalchemy.orm import session
from hashing import hash_password
from fastapi import HTTPException,status
from models import Task, User,Base
Base.metadata.create_all(bind=engine)

app=FastAPI()

# @app.get("/")
# def get_home():
#     return{"welcome": "Maryam"}

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task_create:TaskCreate, db:session=Depends(get_db)):
    task=Task(title=task_create.title, content=task_create.content, description=task_create.description,owner_id=1)
    # task=Task(**task_data.dict()) useful when you have many fields

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.post("/users", response_model=UserResponse)
def create_user(user_create:UserCreate, db:session=Depends(get_db)):
    hashed_pw = hash_password(user_create.password)
    user=User(username=user_create.username,email=user_create.email, password=hashed_pw)
    existing_user= db.query(User).filter(User.username==user_create.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username already exists") 

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db:session=Depends(get_db)):
    tasks=db.query(Task).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id:int,db:session=Depends(get_db)): 
    task=db.query(Task).filter(Task.id==task_id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")   
    return task



@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id:int, task_update:TaskUpdate, db:session=Depends(get_db)):
    task=db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(task,field,value)

    db.commit()
    db.refresh(task)

    return task     


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id:int, db:session = Depends(get_db)):
    task=db.query(Task).filter(Task.id==task_id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= "Task not found")
    
    db.delete(task)
    db.commit()