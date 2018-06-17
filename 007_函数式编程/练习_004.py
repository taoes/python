#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_socre(t):
    return  -t[1]


if __name__ == '__main__':
    L2_by_name = sorted(L, key=by_name)
    L2_by_score = sorted(L, key=by_socre)
    print("by name :", L2_by_name)
    print("by score :", L2_by_score)
