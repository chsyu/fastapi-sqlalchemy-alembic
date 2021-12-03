from fastapi import APIRouter, Depend
from sqlalchemy.orm import Session
from router.schemas import User as SchemaUser
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.post("/user")
def create_user(request: SchemaUser, db: Session = Depends(get_db)):
    return db_user.create_user(request=request, db=db)


@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db=db)

