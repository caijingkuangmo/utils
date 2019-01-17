# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

'''
爬虫过程中，默认发起请求，是去重了的，也就是dont_filter默认为False，
当然不可以不用它的，自定义去重的类 dupefilter类， 其中去重的逻辑就是request_seen里实现
'''

from scrapy.dupefilter import BaseDupeFilter
from scrapy.utils.request import request_fingerprint

class ChoutiDupeFilter(BaseDupeFilter):
    def __init__(self):
        self.visited_fd = set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        fd = request_fingerprint(request=request)
        if fd in self.visited_fd:
            return True
        self.visited_fd.add(fd)

    def open(self):
        print("开始")

    def close(self, reason):
        print("结束")

    def log(self, request, spider):
        print("记录爬取日志")



