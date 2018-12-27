# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/index")
def index():
    return "index"

class MiddleWare:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        print("请求前...")
        result = self.wsgi_app(*args, **kwargs)
        print("请求后...")
        return result

if __name__ == "__main__":
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run()