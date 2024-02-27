from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


# 加上response_model,再加上typing.List,可以返回整个collection
# 加上current_user,可以加上权限
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db),
        ):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,
           db: Session = Depends(database.get_db),
           ):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,
            db: Session = Depends(database.get_db),
            ):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.UpdateBlog,
           db: Session = Depends(database.get_db),
           ):
    return blog.update(id, request, db)


# 加上response_model,会返回你想返回的内容
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int,
         db: Session = Depends(database.get_db),
         ):
    return blog.show(id, db)


# 加上response_model,会返回你想返回的内容
@router.post('/list', status_code=200, response_model=List[schemas.ShowBlog])
def show(request: schemas.SearchBlog, db: Session = Depends(database.get_db)):
    return blog.search(request, db)
