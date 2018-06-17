#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


from functools import partial

if __name__ == '__main__':
    int2bin = partial(int, base=2)
    print("1011(2)= ", int2bin("1011"))
    print("1011(8) = ", int2bin("1011", base=8))
    print("1011(10) = ", int2bin("1011", base=10))
