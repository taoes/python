#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


def lazy_sum(*args):
    def sum_result():
        result = 0
        for x in args:
            result = result + x
        return result
    return sum_result


if __name__ == '__main__':
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_result = lazy_sum(*number)
    result = sum_result()
    print("Result = ", result)
