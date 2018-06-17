#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

import unittest


class Student(object):
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


# 继承 unittest.TestCase即可，以test_开头的均是测试方法
class TestStudent(unittest.TestCase):

    def test_fun_1(self):
        print("执行了test_fun_1()")
        assert len(self.stu) >= 4, "断言失败，名称长度不等于4"

    def test_fun_2(self):
        print("执行了test_fun_2()")
        assert self.stu.name == "Jack", "断言失败,name != jack"

    def normal(self):
        print("执行了普通方法normal()")

    # 测试方法,执行test_之前执行
    def setUp(self):
        self.stu = Student("Jack")
        print("执行了setUp()方法")

    #  特殊测试方法，执行test_之后执行
    def tearDown(self):
        print("执行了tearDown()方法")


if __name__ == '__main__':
    # 执行测试方法
    unittest.main()
