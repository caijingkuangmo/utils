# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class Foo(object):
    def __call__(self, *args, **kwargs):
        print("call")

obj = Foo()
obj()

###########################源码#########################
'''
run_simple 第三参数 + ()  这dm， 执行DispatcherMiddleware的__call__方法

而在上面的__call__方法中，最后flask对象的__call__方法
    源码最后执行了app(environ, start_response)，如果是/sec/index2，那么此时的app就是app2，
是一个flask对象，加括号，会执行里面的__call__,从这里开始又和单app情况下执行流程是一样的
'''

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, current_app

app1 = Flask('app01')

app2 = Flask('app02')


@app1.route('/index')
def index():
    return "app01"


@app2.route('/index2')
def index2():
    return "app2"


# http://www.oldboyedu.com/index
# http://www.oldboyedu.com/sec/index2
dm = DispatcherMiddleware(app1, {
    '/sec': app2,
})

if __name__ == "__main__":
    run_simple('localhost', 5000, dm)