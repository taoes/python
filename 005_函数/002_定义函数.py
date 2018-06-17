#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 定义求解最大值参数
def max_number(numbers):
    return max(numbers)


# 定义求解和函数
def sum_number(numbers):
    return sum(numbers)


# 定义求解平均值函数
def avg_number(numbers):
    result = sum_number(numbers)
    return result / len(numbers)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 3, 2, 1, 0]
    print("The max number is ", max_number(numbers))
    print("The sum is ", sum_number(numbers))
    print("The avg is ", avg_number(numbers))
