# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask
from urls import init_urls

application = Flask(__name__)
application.config.from_object("config.Settings")


for url_dict in init_urls():
    application.add_url_rule(**url_dict)

if __name__ == "__main__":
    application.run()