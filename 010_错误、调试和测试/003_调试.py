#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""


# 调试的方式有很多 print? 断言？ IDEA调试？ 等等，这里我们演示断言以及print

def assert_test(number):
    # 直接打印数据，分析异常
    print(number)
    # 使用断言调试
    assert number % 2 == 0, "断言失败"


if __name__ == '__main__':
    assert_test(2)
    assert_test(4)
    assert_test(5)
