# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")

    db.init_app(app)

    from views.account import account as account_bp
    app.register_blueprint(account_bp, url_prefix="/account")

    return app