from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text, TIMESTAMP, Float
from sqlalchemy import func

from .database import Base
from sqlalchemy.orm import relationship


def getTimeStamp():
    return datetime.now().timestamp()


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)

    articleTitle = Column(String(100))
    articleCover = Column(Text(), default='www.none.com')
    articleContent = Column(Text(),default="{}")

    viewCount = Column(Integer, default=0)
    likeCount = Column(Integer, default=0)
    commentStatus = Column(Boolean, default=0)
    commentCount = Column(Integer, default=0)
    recommendStatus = Column(Boolean, default=1)

    # 时间用时间戳来表示
    createTime = Column(Integer, default=getTimeStamp)
    updateTime = Column(Integer, default=getTimeStamp, onupdate=getTimeStamp)

    # 建立外键 注意是写__tablename__,而不是类名
    userId = Column(Integer, ForeignKey("users.id"))
    sortId = Column(Integer, ForeignKey("blog_sorts.id"))
    labelId = Column(Integer, ForeignKey("blog_labels.id"))
    # 建立关系,不会存到table里的column里
    # 每次query时都会查找creator
    creator = relationship("User", back_populates="blogs")
    sort = relationship("Sort")
    label = relationship("Label")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))
    # 建立关系,不会存到table里的column里
    # 每次query时都会查找blogs
    blogs = relationship("Blog", back_populates="creator")


class Sort(Base):
    __tablename__ = 'blog_sorts'

    id = Column(Integer, primary_key=True, index=True)

    sortName = Column(String(30))
    sortDescription = Column(String(100))

    # 每次query时都会查找labels
    # 此处的labels要和schemas的命名相同
    labels = relationship("Label",back_populates="sort")

    # blogs = relationship("Blog", back_populates="sort")


class Label(Base):
    __tablename__ = 'blog_labels'

    id = Column(Integer, primary_key=True, index=True)

    labelName = Column(String(30))
    labelDescription = Column(String(100))
    sortId = Column(Integer, ForeignKey("blog_sorts.id"))
    
    sort = relationship("Sort",back_populates="labels")
    # blogs = relationship("Blog", back_populates="label")
