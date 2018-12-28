# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Blueprint
from __init__ import db
import models

account = Blueprint("account", __name__)

@account.route("/index")
def index():

    return "index"
