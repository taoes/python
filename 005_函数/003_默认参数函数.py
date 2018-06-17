#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 默认参数
def pow(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


# 可变参数
def add(*numbers):
    sum_number = 0
    for x in numbers:
        sum_number = sum_number + x
    return sum_number


# 关键字参数
def json(name, age, **kwargs):
    print('name:', name, ",age:", age, "other:", kwargs)


if __name__ == '__main__':
    # pow(3) == pow(3,2)
    print("pow(3) = ", pow(3))
    print("pow(4,3) = ", pow(4, 3))
    print("add(1,2,3) = ", add(1, 2, 3))
    print("add(1,2,3,4) = ", add(1, 2, 3, 4))
    number_tuple = [12, 23, 34, 45]
    print("add(*number_tuple) = ", add(*number_tuple))
    # Error
    # print("add(number_tuple) = ", add(number_tuple))
    json("Tom", 12)
    json("Smith", 22, address="AnHui", gradle=90)
    person = {"life": 12, "father": "Tom"}
    json("Mary", 12, **person)
