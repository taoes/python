#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
import math


def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return None, None
    num_1 = (-b + math.sqrt(delta)) / (2 * a)
    num_2 = (-b - math.sqrt(delta)) / (2 * a)
    return num_1, num_2


# 求解一元二次方程
if __name__ == '__main__':
    x1, x2 = quadratic(1, 2, -15)
    print("x1 = %f,x2 = %f" % (x1, x2))
