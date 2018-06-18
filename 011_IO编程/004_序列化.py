#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

import pickle, json


class Student(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return str({"name": self.name, "age": self.age, "address": self.address})


def test_class_pickle():
    stu = Student("Jack", 12, "Bozhou AnHui China")
    print("原对象内容：", stu)
    stu.name = "Smith"
    print("修改之后的内容：", stu)
    # 序列化
    with open("disk/stu.data", "wb") as file:
        pickle.dump(stu, file)

    # 反序列化
    with open("disk/stu.data", "rb") as file:
        stu1 = pickle.load(file)
        print("反序列化结果", stu1)

    # 使用JSON序列化
    print("JSON序列化:", json.dumps(stu, default=lambda obj: obj.__dict__))


if __name__ == '__main__':
    test_class_pickle()
