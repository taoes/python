#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 使用迭代查找一个list中最小和最大值，并返回一个tuple：
def find_min_and_max(L):
    if len(L) == 0:
        return None, None
    max_result = L[0]
    min_result = L[0]
    for number in L:
        if number > max_result:
            max_result = number
        if number < min_result:
            min_result = number
    return min_result, max_result


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
