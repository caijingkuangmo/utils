# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

'''
不同路由间临时数据共享，
比如：正常访问发生错误，共享错误信息
'''
from flask import Flask, flash, get_flashed_messages, redirect, request

app = Flask(__name__)
app.secret_key = "hehe"

@app.route('/index')
def index():
    val = request.args.get("v")
    if val == "hello":
        return "hello world"
    flash("超时错误", category="x1")
    return redirect("/error")

@app.route("/error")
def error():
    """
    展示错误信息
    :return:
    """
    msg = get_flashed_messages(category_filter=["x1"])
    print("msg", msg)
    if msg:
        error_msg = msg[0]
    else:
        error_msg = "..."
    return error_msg

if __name__ == "__main__":
    app.run()