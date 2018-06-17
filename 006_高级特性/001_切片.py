#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

# List切片

numbers = list(range(100))

print("第10个数字：", numbers[10])
print("倒数第10个数字：", numbers[-10])

# 前置包括后置不包括
print("第3个到第8个数字", numbers[3:8])
print("倒数第8个到倒数第3个", numbers[-8:-3])

print("每隔21个取出一个:", numbers[::21])
print("前50个数每隔9个取出一个:", numbers[:50:9])
