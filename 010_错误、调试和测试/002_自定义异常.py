#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
import logging


class NotFoundError(BaseException):
    def __init__(self, message):
        self.message = message


def find_substr(str):
    if "abc" not in str:
        raise NotFoundError("没有发现abc字符串")


if __name__ == '__main__':
    try:
        find_substr("abcdefg")
        find_substr("acd")
    except NotFoundError as error:
        logging.error("捕捉到 NotFoundError 异常", error)
