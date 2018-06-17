#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
from collections import Iterable

name = "Smith"
for index,char in enumerate(name):
    print("index = %d , char = %s" % (index,char))

dic = {"name": "Tom", "age": 12, "grade": 12.12}
for key in dic:
    print("\nkey = %s value = %s" % (key, dic.get(key)))

print("字符串可迭代:", isinstance("ABC", Iterable))
print("List可迭代:", isinstance([1, 2, 3, 4], Iterable))
print("整数可迭代:", isinstance(12, Iterable))
