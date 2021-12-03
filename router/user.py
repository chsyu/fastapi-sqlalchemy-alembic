from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import User as SchemaUser
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.post("/user", response_model=SchemaUser)
def create_user(request: SchemaUser, db: Session = Depends(get_db)):
    return db_user.create_user(request=request, db=db)


@router.get("/users", response_model=List[SchemaUser])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db=db)

