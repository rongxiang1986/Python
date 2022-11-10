#!/usr/bin/python
# -*- coding: UTF-8 -*-

class SelfExceptionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise SelfExceptionError('用户自定义异常')
except SelfExceptionError as e:
    print('user self defined exception occurred', e.msg)
