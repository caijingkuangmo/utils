# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __init__ import db, create_app

app = create_app()

with app.app_context():
    db.create_all()