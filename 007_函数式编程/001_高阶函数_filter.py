#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


def filter_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    numbers = list(range(20))
    print("Even = ", list(filter(filter_even, numbers)))
