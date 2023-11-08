from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session


def create(request: schemas.User, db: Session):
    new_sort = models.Sort(
        sortName=request.sortName,
        sortDescription=request.sortDescription,
    )
    db.add(new_sort)
    db.commit()
    db.refresh(new_sort)
    return new_sort


def show(id: int, db: Session):
    if id == -1:
        sort = db.query(models.Sort).all()
    else:
        sort = db.query(models.Sort).filter(models.Sort.id == id).first()
        
    print(sort[0].labels[0].labelName)

    if not sort:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Sort with the id {id} is not available')
    return sort
