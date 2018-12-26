# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, views

app = Flask(__name__)
app.config['DEBUG'] = True

def auth(func):
    def inner(*args, **kwargs):
        print("执行登录验证")
        result = func(*args, **kwargs)
        return result
    return inner

class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [auth,]

    def get(self):
        return "Index.GET"

    def post(self):
        return "Index.POST"

app.add_url_rule('/index', view_func=IndexView.as_view(name="index"))

if __name__ == "__main__":
    app.run(host="localhost", port=5566)

