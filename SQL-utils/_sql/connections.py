# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import models


settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "123456",
    "db": "dbtwo"
}

# pymysql  原生sql
import pymysql
class SqlConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = pymysql.connect(**settings)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

######################################
# sqlalchemy 原生sql
from sqlalchemy import create_engine

class SqlAlchemyConnection:
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/dbtwo?charset=utf8", max_overflow=5)
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = self.engine.raw_connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

############################################
# sqlalchemy 对象，连接池方式
from sqlalchemy.orm import sessionmaker

class AlchemyConnection:
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:123456@127.0.0.1:3306/dbtwo?charset=utf8",
            max_overflow=0,  # 超过连接池大小外最多创建的连接
            pool_size=5,  # 连接池大小
            pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
            pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        )
        self.session = sessionmaker(bind=self.engine)
        self.conn = None

    def __enter__(self):
        self.conn = self.session()
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


# 基础连接测试
# with SqlConnection() as conn:
#     result = conn.cursor.execute("select * from app01_classlist")
#     print(result)
#     result2 = conn.cursor.fetchone()
#     print(result2)

# with SqlAlchemyConnection() as conn:
#     result = conn.cursor.execute("select * from app01_classlist")
#     print(result)
#     result2 = conn.cursor.fetchone()
#     print(result2)

# with AlchemyConnection() as session:
#     results = session.query(models.ClassList).all()
#     for result in results:
#         print(result.caption)