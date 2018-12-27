# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'


class Config(object):
    DEBUG = False  #是否开始Debug模式
    TESTING = False   #是否开始测试模式
    SECRET_KEY = "hehe"
    DATABASE_URI = "sqlite://:memory:"

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