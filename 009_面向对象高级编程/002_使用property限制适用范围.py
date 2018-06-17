#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


class Student(object):

    @property
    def score(self):
        return self.__score

    def __init__(self, score):
        if not isinstance(score, int):
            raise TypeError("score must is an int type")

        if score > 100 or score < 0:
            raise ValueError("score must between 0~100")
        self.__score = score


if __name__ == '__main__':
    stu = Student(100)
    print("Score is %d" % stu.score)
    # AttributeError: can't set attribute
    # stu.score = 99
    # print("Score is %d" % stu.score)
