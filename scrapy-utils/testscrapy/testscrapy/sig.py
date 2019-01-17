# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from scrapy import signals

'''
使用框架预留的位置，帮助你自定义一些功能。
EXTENSIONS = {
    'xdb.ext.MyExtend':666,
}
'''

class MyExtend(object):
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        self = cls()

        crawler.signals.connect(self.x1, signal=signals.spider_opened)
        crawler.signals.connect(self.x2, signal=signals.spider_closed)

        return self

    def x1(self, spider):
        print('open')

    def x2(self, spider):
        print('close')
