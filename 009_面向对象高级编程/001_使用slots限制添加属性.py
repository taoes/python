#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性.

class Student(object):
    pass


# __slots__ 对继承的子类无效
class People(object):
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    # Student未使用__slots__限制,因此可以随意添加
    stu = Student()
    stu.name = "Jack"
    stu.age = 18
    stu.score = 100
    print("name = %s age = %d score = %d" % (stu.name, stu.age, stu.score))

    # People使用了限制
    people = People()
    people.name = "Smith"
    people.age = 12
    # AttributeError: 'People' object has no attribute 'address
    # people.address = "AnHui"
