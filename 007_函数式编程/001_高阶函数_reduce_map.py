#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
from functools import reduce


# 计算数字的平方
def squares(number):
    return number * number


def list2int(x, y):
    return x * 10 + y


if __name__ == '__main__':
    # list()将Iterator 惰性序列转换为list
    numbers = list(range(10))
    # 将函数作为参数传递
    result = map(squares, numbers)
    print("result = ", list(result))
    # 将一个list转化为一个数字
    numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print("result = ", reduce(list2int, numbers))
