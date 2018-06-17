#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
import logging


# 纯属为了演示错误的传递
def str2int(x: str):
    return int(x)


def division(x: str, y: str):
    return str2int(x) / str2int(y)


if __name__ == '__main__':
    try:
        print(" 3 / 2 == ", division("3", "2"), end=" ")
    except BaseException as error:
        print("捕捉到了异常信息")
    else:
        print("没有发现异常")

    try:
        print(" 3 / 0 == ", division("3", "0"))
    except ZeroDivisionError as error:
        logging.error("捕获到除以0异常")

    try:
        print("3 / a == ", division("2", "a"))
    except ValueError as verror:
        logging.error("捕捉到值错误")
