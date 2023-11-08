from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import sort
from typing import List

router = APIRouter(
    prefix="/sort",
    tags=['Sorts']
)


@router.post('/', response_model=List[schemas.Sort])
def get_all_sort(db: Session = Depends(database.get_db)):
    return sort.show(-1, db)


@router.post('/create', response_model=schemas.Sort)
def create_sort(request: schemas.SortBase, db: Session = Depends(database.get_db)):
    return sort.create(request, db)


@router.get('/{id}', response_model=schemas.Sort)
def get_user_byId(id: int, db: Session = Depends(database.get_db)):
    return sort.show(id, db)
