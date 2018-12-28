# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __init__ import db


class Users(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.username
