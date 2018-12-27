# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class Foo(object):
    def __init__(self):
        self.name = "alex"
        self.__age = 18

    def get_age(self):
        return self.__age

obj = Foo()
print(obj.get_age())
# print(obj.__age)
print(obj._Foo__age) #强制调用私有变量

######################源码##############################

'''
在flask实例request时，也就是LocalProxy对象，传入偏函数(也就是这里local)

执行init方法里就用到 强制设置私有__local
def __init__(self, local, name=None):
    object.__setattr__(self, '_LocalProxy__local', local)
    object.__setattr__(self, '__name__', name)
    if callable(local) and not hasattr(local, '__release_local__'):
        # "local" is a callable that is not an instance of Local or
        # LocalManager: mark it as a wrapped function.
        object.__setattr__(self, '__wrapped__', local)
'''
