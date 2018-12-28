# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, request

app = Flask(__name__)

@app.route("/index")
def index():

    return "index"

app.wsgi_app
if __name__ == "__main__":
    app.run(port=9999)