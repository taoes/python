#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


def read_config():
    with open("disk/example_002.txt", 'r', encoding="utf8") as file:
        text = file.read()
        print(text)

if __name__ == '__main__':
    read_config()
