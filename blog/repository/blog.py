from datetime import datetime
from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_


def get_all(db: Session):
    Blog = models.Blog

    blogs = db.query(Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    Blog = models.Blog

    new_blog = Blog(
        articleTitle=request.articleTitle,
        articleCover=request.articleCover,
        articleContent=request.articleContent,
        userId=request.userId,
        sortId=request.sortId,
        labelId=request.labelId,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    Blog = models.Blog

    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.delete()
    db.commit()
    return {'done': 'nice delete!'}


def update(id: int, request: schemas.UpdateBlog, db: Session):
    Blog = models.Blog

    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.update({
        'articleTitle': request.articleTitle,
        'articleCover': request.articleCover,
        'articleContent': request.articleContent,
        'updateTime': datetime.now().timestamp()
    })
    # 用不了此方法,草了
    # blog.update(request)
    # print(request.items())
    db.commit()
    return {
        'msg': 'update success!'
    }


def show(id: int, db: Session):
    Blog = models.Blog

    blog = db.query(Blog).filter(Blog.id == id)

    blog.update({
        'viewCount': Blog.viewCount + 1
    })
    db.commit()
    # 回应查询错误
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog.first()


def search(request: schemas.SearchBlog, db: Session):
    Blog = models.Blog

    # 构建查询
    query = db.query(Blog)

    # 根据参数应用过滤条件
    if request.sortId > 0:
        query = query.filter(Blog.sortId == request.sortId)
        if request.labelId > 0:
            query = query.filter(and_(
                Blog.sortId == request.sortId, Blog.labelId == request.labelId))
    if len(request.articleSearch) > 0:
        # 无视大小写 模糊搜索
        query = query.filter(Blog.articleTitle.ilike(
            f"%{request.articleSearch.lower()}%"))
    else:
        query = query.filter()

    # 按时间排序(一定要在分页前面写才有效)
    query = query.order_by(Blog.createTime.desc())

    # 分页
    if request.current and request.size:
        query = query.limit(request.size).offset(
            (request.current - 1) * request.size)

    # 获取总记录数
    total = query.count()

    blog = query.all()
    # 回应查询错误
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog is not available')
    print(total)
    return blog
