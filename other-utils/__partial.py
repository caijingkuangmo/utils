# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import functools


def func(a1, a2):
    print(a1)
    print(a2)


# 重新封装成一个 给前面参数加默认值 的函数
new_func = functools.partial(func, 666)
new_func(777)

###########################源码############################