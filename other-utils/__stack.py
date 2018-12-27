# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

'''
在flask源码中，存储RequestContent对象就是用的栈，操作者LocalStack对象就负责维持和操作栈
    def push(self, obj):
        rv = getattr(self._local, 'stack', None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(obj)
        return rv

    def pop(self):
        stack = getattr(self._local, 'stack', None)
        if stack is None:
            return None
        elif len(stack) == 1:
            release_local(self._local)
            return stack[-1]
        else:
            return stack.pop()

    @property
    def top(self):
        try:
            return self._local.stack[-1]
        except (AttributeError, IndexError):
            return None

'''

'''
访问频率控制则用是 先进先出模式，看似队列，严格意思上不算，因为在内存级别位置发生变化

频率控制原理:
    一般登录用户，用用户名控制，而匿名用户，用IP来控制
    控制过程一般是：拿IP举例，维持一个以IP为键，登录时间戳队列为值的字典，每次判断时先把时间戳队列中的超时时间删掉，
    统计队列中剩余时间戳个数来做频率控制
'''
from rest_framework.throttling import BaseThrottle


class VisitThrottle(BaseThrottle):
    '''
    一分钟内访问超过5次  禁用两分钟
    '''

    VISIT_RECORD = {}

    def allow_request(self, request, view):
        remote_addr = request.META.get('REMOTE_ADDR')
        print(remote_addr)
        now_time = time.time()

        if remote_addr not in VisitThrottle.VISIT_RECORD:
            VisitThrottle.VISIT_RECORD[remote_addr] = {
                'start_time': [now_time, ],
                'forbid': False
            }
            return True

        start_time = VisitThrottle.VISIT_RECORD[remote_addr]['start_time']
        forbid_state = VisitThrottle.VISIT_RECORD[remote_addr]['forbid']
        while start_time and start_time[-1] < now_time - 60 and not forbid_state:
            start_time.pop()

        if forbid_state:
            if now_time - start_time[-1] > 120:
                print('两分钟过了，解禁')
                VisitThrottle.VISIT_RECORD[remote_addr] = {
                    'start_time': [now_time, ],
                    'forbid': False
                }
                print(VisitThrottle.VISIT_RECORD[remote_addr])
                return True
            else:
                print("两分钟内禁止访问，已经过了%s秒" % (now_time - start_time[-1]))
                return False
        else:
            if len(start_time) < 5:
                print("访问%s次" % (len(start_time) + 1))
                print(start_time)
                start_time.insert(0, now_time)
                return True
            else:
                print("访问%s次，禁止访问" % len(start_time))
                VisitThrottle.VISIT_RECORD[remote_addr] = {
                    'start_time': [now_time, ],
                    'forbid': True
                }
                return False