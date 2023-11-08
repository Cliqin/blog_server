from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session


def create(request: schemas.UserBase, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password
        # password=Hash.bcrypt(request.password)  # 将密码进行hash加密
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user
