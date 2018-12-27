# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

'''
before request 按照定义顺序从上往下执行
after request 按照定义顺序从下往上执行

errorhandler 定义错误页面

定义之后直接在模板中可以调用，和django的simple_tag很像
template_global  {{shaobing(1,2)}}
template_filter  {{ 1|db(2,3)}}
'''

from flask import Flask, Request, render_template

app = Flask(__name__, template_folder="templates")
app.debug = True

@app.before_first_request
def before_first_request1():
    print("first request")

@app.before_first_request
def before_first_request2():
    print("first request2")

@app.before_request
def before_request1():
    print("before request1")

@app.after_request
def after_request1(response):
    print("after_request1")
    return response

@app.after_request
def after_request2(response):
    print("after_request2")
    return response

@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist", 404


@app.template_global()
def shaobing(a1, a2):
    return a1 + a2

@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3

@app.route("/")
def index():
    return render_template("hello.html")



if __name__ == "__main__":
    app.run()