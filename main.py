import uvicorn
from fastapi import FastAPI, HTTPException

import os
from fastapi import Depends
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import User as ModelUser
from schema import User as SchemaUser
from dotenv import load_dotenv
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()
db_url="postgresql+psycopg2://postgres:postgres@db:5432"
# app.add_middleware(DBSessionMiddleware, db_url)
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user", response_model=SchemaUser)
def create_user(user: SchemaUser, db: Session = Depends(get_db)):
    db_user = ModelUser(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.add(db_user)
    db.commit()
    return db_user


@app.get("/users", response_model=List[SchemaUser])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(ModelUser).all()
    if not users:
        raise HTTPException(status_code=404,
                            detail=f'Users not found')
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
