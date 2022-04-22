from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import  List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):

    # hash password
    user.password = utils.hash(user.password)
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_post(id : int, db: Session = Depends(get_db)):
    post = db.query(models.User).filter(models.User.user_id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} not Exists")
    return post