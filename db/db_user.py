from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from router.schemas import User as SchemaUser
from .models import User as ModelUser


def create_user(request: SchemaUser, db: Session):
    db_user = ModelUser(
        first_name=request.first_name,
        last_name=request.last_name,
        age=request.age
    )
    db.add(db_user)
    db.commit()
    return db_user
    # return "a user has been created"


def get_all_users(db: Session):
    users = db.query(ModelUser).all()
    if not users:
        raise HTTPException(status_code=404,
                            detail=f'Users not found')
    return users
    # return "all users have gotten"
