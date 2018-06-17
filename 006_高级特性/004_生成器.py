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


# 使用生成器生成
def generator():
    return (x * x for x in range(10))


if __name__ == '__main__':
    print("normal_function() = ", normal_function())
    print("list_generator() = ", list_generator())
    # 重点
    print("generator() = ")
    for x in generator():
        print(x, end=',')
