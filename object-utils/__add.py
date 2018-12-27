# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class Foo(object):

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        data = self.num + other.num
        return Foo(data)

obj1 = Foo(11)
obj2 = Foo(22)
v = obj1 + obj2
print(v.num)

##############################源码################################