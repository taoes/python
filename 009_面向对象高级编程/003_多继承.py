#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, content):
        print("%s is speak %s" % (self.name, content))


class Study(object):
    def __init__(self, name):
        self.name = name

    def learning(self):
        print("%s is learning....." % self.name)


# Student 继承了People & Study
class Student(People, Study):

    def __init__(self, name, age):
        People.__init__(self, name, age)
        Study.__init__(self, name)


if __name__ == '__main__':
    stu = Student("Mary", 12)
    stu.learning()
    stu.speak("One World,One Dream!")
