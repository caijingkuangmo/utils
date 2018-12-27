# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class Foo(object):
    def __init__(self):
        # self.storage = {}  #这里也会执行__setattr__方法
        object.__setattr__(self, "storage", {})  #调用父类的__setattr__方法设置，就不会调用当前类里的__setattr__方法

    def __getattr__(self, item):
        print(item)

    def __setattr__(self, key, value):
        print(key, value)

    def __delattr__(self, item):
        print(item)

obj = Foo()
obj.x = 123  #调用__setattr__方法
obj.x       #调用__getattr__方法
del obj.x   #调用__delattr___方法
'''
执行结果
storage {}
x 123
x
x
'''

##########################源码########################
#flask实现不同线程存值  Local类

"""
local中的存储结构：
{
    线程id/协程id:{
        username:"alex",
    }
    线程id/协程id:{
        username:"alex",
    }
}
"""

import threading

try:
    from greenlet import getcurrent as get_ident  # 协程
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident  # 线程


class Local(object):

    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


local_values = Local()


def task(num):
    local_values.name = num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,), name='线程%s' % i)
    th.start()

'''
在flask视图中，执行request.method，会执行LocalProxy的__getattr__方法，
在这方法中最终执行偏函数获取requestContent对象，然后映射method取值
'''