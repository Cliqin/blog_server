from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import label
from typing import List

router = APIRouter(
    prefix="/label",
    tags=['Labels']
)


@router.post('/', response_model=List[schemas.Label])
def get_all_label(db: Session = Depends(database.get_db)):
    return label.show(-1, db)


@router.post('/create', response_model=schemas.Label)
def create_label(request: schemas.LabelBase, db: Session = Depends(database.get_db)):
    return label.create(request, db)


@router.get('/{id}', response_model=schemas.Label)
def get_label_byId(id: int, db: Session = Depends(database.get_db)):
    return label.show(id, db)
