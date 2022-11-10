#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback
import sys

f = open("test.txt", "r")

try:
    f.write("写入内容")
except IOError as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("exc_type:", exc_type)
    print("exc_value:", exc_value)
    print("exc_traceback:", exc_traceback)
    print("----")
    traceback.print_exc()
    traceback.print_tb(exc_traceback)
    traceback.format_exc()
    traceback.print_exception(exc_type, exc_value, exc_traceback)

else:
    print("写入文件成功")
finally:
    f.close()

"""
not writable
Traceback (most recent call last):
  File "D:/git/Python/bestPractice/exceptionExample/example3.py", line 8, in <module>
    f.write("写入内容")
io.UnsupportedOperation: not writable
"""