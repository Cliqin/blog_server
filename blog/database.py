from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

pymysql.install_as_MySQLdb()

# 要操作的数据库路径
SQLALCHAMY_DATABASE_URL = 'mysql://root:123456@localhost:3306/myblog'
# SQLALCHAMY_DATABASE_URL = 'mysql://newfastapi:123456@localhost:3306/myblog'
engine = create_engine(
    SQLALCHAMY_DATABASE_URL
)

# 创造数据库操作对象
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# 注册models要用到的base
Base = declarative_base()


# 定义一个获取数据库的“生成器”,到时候给api用
# 语法看不太懂,迟点再深究
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
