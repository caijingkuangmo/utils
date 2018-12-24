# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/index')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()