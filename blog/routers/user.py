from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/create', response_model=schemas.User)
def create_user(request: schemas.UserBase, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)
