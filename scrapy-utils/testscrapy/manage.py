# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import sys
from scrapy.cmdline import execute

if __name__ == "__main__":
    execute("scrapy crawl chouti --nolog".split())