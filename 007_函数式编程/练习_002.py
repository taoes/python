#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

# Python提供的sum()函数可以接受一个list并求和
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# -*- coding: utf-8 -*-
from functools import reduce


def multiplication(x, y):
    return x * y


def prod(L):
    if len(L) == 0:
        return 0
    return reduce(multiplication, L)


if __name__ == '__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
