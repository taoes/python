#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


class People(object):
    __is_gay: bool
    name: str = None

    def __init__(self, name):
        self.name = name
        self.__is_gay = False

    def get_name(self):
        return self.name


if __name__ == '__main__':
    people = People("Smith")
    print("Your name's ", people.get_name())
    # 'People' object has no attribute '__is_gay'
    try:
        people.__is_gay
    except AttributeError:
        print("No __is_gay__")
