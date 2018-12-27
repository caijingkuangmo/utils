# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from itertools import chain

v1 = [11, 22, 33]
v2 = [44, 55, 66]

new = chain(v1, v2)
for item in new:
    print(item)


def f1(x):
    return x + 1


func1_list = [f1, lambda x: x - 1]


def f2(x):
    return x + 10


new_func_list = chain([f2], func1_list)
for func in new_func_list:
    print(func)


#################################源码#########################