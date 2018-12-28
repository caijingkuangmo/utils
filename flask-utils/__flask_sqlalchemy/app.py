# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven

from flask import Flask
from __init__ import create_app

app = create_app()

@app.route("/")
def index():
    return "Index"

if __name__ == "__main__":
    app.run()