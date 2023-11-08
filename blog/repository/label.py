from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session


def create(request: schemas.User, db: Session):
    new_label = models.Label(
        labelName=request.labelName,
        labelDescription=request.labelDescription,
        sortId = request.sortId
        
    )
    db.add(new_label)
    db.commit()
    db.refresh(new_label)
    return new_label


def show(id: int, db: Session):
    if id == -1:
        label = db.query(models.Label).all()
    else:
        label = db.query(models.Label).filter(models.Label.id == id).first()
        
    print(label[0].sort.sortName)
    if not label:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Label with the id {id} is not available')
    return label
