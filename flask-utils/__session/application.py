# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, session, render_template, request, redirect, url_for

from flask.ext.session import Session
app = Flask(__name__)
# app.config['SECRET_KEY'] = "heihei"
app.debug = True
app.secret_key = "heihei"

# session 引入第三方服务
app.config['SESSION_TYPE'] = 'redis'
from redis import Redis
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1',port='6379')
Session(app)

@app.route('/index', endpoint="index")
def index():
    if not session.get("username"):
        return redirect(url_for("login"))
    return "index"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username"):
            session["username"] = request.form.get("username")
            return redirect(url_for("index"))
    return """
    <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run()