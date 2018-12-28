# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'


class Config(object):
    DEBUG = False  #是否开始Debug模式
    TESTING = False   #是否开始测试模式
    SECRET_KEY = "hehe"
    DATABASE_URI = "sqlite://:memory:"

    # 需要配合flask-sqlalchemy组件使用
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3306/s7day145_2?charset=utf8"
    # SQLALCHEMY_POOL_SIZE = 5
    # SQLALCHEMY_POOL_TIMEOUT = 30
    # SQLALCHEMY_POOL_RECYCLE = -1

class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


'''
1.字符串分割rsplit
2.import_lib导入模块
3.getattr获取类
'''