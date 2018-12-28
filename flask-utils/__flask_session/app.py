# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, session

app = Flask(__name__)
app.secret_key = "heihei"

# #方式一
# #指定 session_interface类
# from redis import Redis
# from flask_session import RedisSessionInterface
#
# conn = Redis(host="localhost", port=6379)
# #permanent为True时，关闭浏览器，cookie就失效
# app.session_interface = RedisSessionInterface(conn, key_prefix="__", use_signer=False, permanent=True)

#方式二
#配置文件方式
from redis import Redis
from flask_session import Session
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host="localhost", port=6379)
Session(app)


@app.route("/")
def index():
    session['xxx'] = 123
    return "Index"

if __name__ == "__main__":
    app.run()

'''
源码解析：
    请求刚到来，获取随机字符串，有就去“数据库，比如redis，文件，数据库”中获取原来的个人数据，否则创建一个空的容器(特殊的字典，比如SecureCookieSession，存在随机字符串)
    视图：操作 内存中的特殊字典（随机字符串 ，存放数据容器）
    响应：把内存对象数据保存到数据库中，并把随机字符串更新到用户的cookie中

    第二种方式，本质就是第一方式的工厂模式版本，在Session(app)里会调用init_app(app)
        通过工厂模式从配置文件获取配置信息，然后指定session_interface
        if config['SESSION_TYPE'] == 'redis':
            session_interface = RedisSessionInterface(
                config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'memcached':
            session_interface = MemcachedSessionInterface(
                config['SESSION_MEMCACHED'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'filesystem':
            session_interface = FileSystemSessionInterface(
                config['SESSION_FILE_DIR'], config['SESSION_FILE_THRESHOLD'],
                config['SESSION_FILE_MODE'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'mongodb':
            session_interface = MongoDBSessionInterface(
                config['SESSION_MONGODB'], config['SESSION_MONGODB_DB'],
                config['SESSION_MONGODB_COLLECT'],
                config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
                config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'sqlalchemy':
            session_interface = SqlAlchemySessionInterface(
                app, config['SESSION_SQLALCHEMY'],
                config['SESSION_SQLALCHEMY_TABLE'],
                config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
                config['SESSION_PERMANENT'])
        else:
            session_interface = NullSessionInterface()
'''