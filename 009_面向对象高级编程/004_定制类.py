#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


class People(object):

    # init 是初始化函数
    def __init__(self, name, age, hight):
        self.name = name
        self.age = age
        self.len = hight

    # 重写此函数可以使用len()函数
    def __len__(self):
        return self.len

    # 重写此函数可以避免如下的输出
    # <__main__.Student object at 0x109afb190>
    def __str__(self):
        return str({"name": self.name, "age": self.age})

    # 当没有找到属性名称的时候在此处查找
    def __getattr__(self, item):
        return "%s not found" % item

    # 直接使用实例调用此方法
    def __call__(self, *args, **kwargs):
        return "调用了call()函数"


if __name__ == '__main__':
    people = People("Jack", 18, 172)
    print("People 输出 = ", people)
    print("People 长度  = ", len(people))
    print("People.address  = ", people.address)
    # 通过callable()判断是否是可调用对象
    print("people() callable ？ ", callable(people))
    print("people() = ", people())
