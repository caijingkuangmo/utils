# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from views import *

urls_map = [
    ('/login', 'login', login, ['GET', 'POST']), # 匹配规则，别名，视图函数，允许请求类型
    ('/hello', 'hello', hello, ['GET', 'POST']),
]

def init_urls():
    return [{
        "rule" : url_item[0],
        "endpoint" : url_item[1] or None,
        "view_func" : url_item[2] or None,
        "methods" : url_item[3] or None
    } for url_item in urls_map]