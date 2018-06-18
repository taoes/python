#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

from io import StringIO

if __name__ == '__main__':
    text = StringIO()
    text.write("I am Student.\nI from AnHui China.")
    text.write("\nI like Code.")
    # getValue用于获取write之后的数据
    str = text.getvalue()
    print(str)
