# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class Foo(object):

    # def __str__(self):
    #     return "foo"

    def __repr__(self):  #终端显示内容，print时，没有__str__方法，打印这个
        return "<Foo>"

obj = Foo()
print(obj)


################################源码############################

'''
在打印flask的request时，就会执行LocalProxy的__str__方法
__str__ = lambda x: str(x._get_current_object())
它又会执行LocalProxy下的_get_current_object方法，而它里面就是执行__local + （）执行偏函数
偏函数，获取requestContent对象，映射获取(比如request,session)对象返回
'''