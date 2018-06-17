#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 生成0-10的平方数

# 普通方式遍历生成
def normal_function():
    result = []
    for x in range(10):
        result.append(x * x)
    return result


# 使用列表生成器
def list_generator():
    return [x * x for x in range(10)]


# 生成0-20之间的偶数的平方
def list_generator_even():
    return [x * x for x in range(20) if x % 2 == 0]


# 双重生成器
def list_generator_double(str1, str2):
    return [x + y for x in str1 for y in str2 if x != y]


if __name__ == '__main__':
    print("normal_function() = ", normal_function())
    print("list_generator() = ", list_generator())
    print("0-20 of the even number of squares = ", list_generator_even())
    # 两个数字123，789 的全排列
    print("123 ， 125 = ", list_generator_double("123", "125"))
