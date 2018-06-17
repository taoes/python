#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

# -*- coding: utf-8 -*-
from functools import reduce


def str2int(char):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[char]


def mul(x, y):
    return 10 * x + y


def str2float(s):
    result = map(str2int, [x for x in s if x != '.'])
    return reduce(mul, result) / pow(10, len(s) - s.index('.') - 1)


if __name__ == '__main__':
    print('str2float(\'123.45632\') =', str2float('123.45632'))
    if abs(str2float('123.45632') - 123.45632) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
