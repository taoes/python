#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 定义一个动物类
class Animal(object):

    def __init__(self, name):
        self.name = name

    def run(self):
        print("Animal %s is Runing..." % self.name)

    def eat(self):
        print("Animal %s is Eating...." % self.name)


# 定义一个🐶
class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)


# 定义一个🐱
class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def eat_fish(self):
        print("%s is eating fish..." % self.name)


if __name__ == '__main__':
    # 继承
    dog = Dog("DOG")
    dog.run()
    dog.eat()

    cat = Cat("CAT")
    cat.run()
    cat.eat()
    cat.eat_fish()

    # 多态
    animal = Cat("cat")
    animal.run()
    # 注意此处和静态语言的区别
    animal.eat_fish()
