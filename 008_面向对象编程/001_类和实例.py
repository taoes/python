#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


class Student(object):

    # 定义初始化函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义普通函数--获取学生信息
    def get_info(self):
        print("name = %s ,age = %d " % (self.name, self.age))

    # 定义普通函数--是否成年
    def is_adult(self):
        return self.age >= 18


if __name__ == '__main__':
    stu = Student("Jack", 24)
    stu.get_info()
    print("是否成年 = ", stu.is_adult())
