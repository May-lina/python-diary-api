from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# print("SQLite DB path:", os.path.abspath("diary.db"))

SQLALCHEMY_DATABASE_URL="sqlite:///./diary.db"

engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

session_local=sessionmaker(bind=engine, autoflush=False, autocommit=False) 

# Base=declarative_base

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()    

