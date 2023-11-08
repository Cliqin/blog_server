from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

'''基础类'''


class BlogBase(BaseModel):
    sortId: int
    labelId: int
    articleTitle: str
    articleCover: str
    articleContent: str
    
    class Config:
        orm_mode = True


class Blog(BlogBase):
    userId: int

    class Config:
        orm_mode = True


class UpdateBlog(BaseModel):
    articleTitle: str
    articleCover: str
    articleContent: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True





class SortBase(BaseModel):
    sortName: str
    sortDescription: str

    class Config:
        orm_mode = True

class LabelBase(BaseModel):
    labelName: str
    labelDescription: str
    sortId:int

    class Config:
        orm_mode = True


class Label(LabelBase):
    id: int
    sort: SortBase



class Sort(SortBase):
    id: int
    labels:List[LabelBase]=[]

class attachUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class attachLabel(LabelBase):
    id: int
    
class attachSort(SortBase):
    id: int

class Sort(SortBase):
    id: int
    labels:List[attachLabel]=[]


class ShowBlog(BlogBase):
    id: int

    viewCount: int
    likeCount: int
    commentStatus: int
    createTime: int
    updateTime: int

    # relationship
    creator: attachUser
    label: attachLabel
    sort: attachSort

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    blogs: List[ShowBlog] = []

class SearchBlog(BaseModel):
    current: int  # 当前页面
    size: int  # 每页多少
    total: int  # 已经展示了的数量
    searchKey: str = ""
    sortId: int  # 分类id
    labelId: int  # 标签id
    articleSearch: str = ""
