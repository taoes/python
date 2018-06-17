#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
import math

if __name__ == '__main__':
    Pythagorean = lambda x, y: math.sqrt(x * x + y * y)
    result = Pythagorean(3, 4)
    print("Result = ", result)
