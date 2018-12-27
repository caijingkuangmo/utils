#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from .config import DevelopmentConfig
from .admin import admin as admin_bp
from .web import web as web_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(web_bp)
