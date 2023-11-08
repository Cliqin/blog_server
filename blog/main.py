from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, sort, label

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 在数据库生成表
models.Base.metadata.create_all(engine)

# 此处仅配置允许跨域请求的源列表
# allow_origins = ['*']
# app.add_middleware(CORSMiddleware, allow_origins=allow_origins)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 登记路由信息
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(sort.router)
app.include_router(label.router)
