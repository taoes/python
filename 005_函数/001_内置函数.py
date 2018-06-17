#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

print("--------ABS-----------")
print("abs(-10) = ", abs(-10))
print("abs(-9.99999) = ", abs(-9.9999))
absi = abs

print("absi(-12) = ", absi(-12))

print("--------MAX & MIN-----------")
print("max = ", max([10, 2, 112, 324, 12, -12]))
print("min = ", min([10, 2, 112, 324, 12, -12]))

print("--------Type Convert-----------")
print('str 2 int ', int('123'))
print('str 2 float ', float('123'))
print('float 2 str ', str(123.093123))
print('int 2 bool ', bool(1))
print('str 2 bool ', bool(' '))
print('str 2 bool ', bool(' '))
print('str 2 bool ', bool(''))
