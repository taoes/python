#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

sum = 0
number = 100

while number > 0:
    sum = sum + number
    number = number - 1
print("1 + 2 + 3 + ....+ 100 =", sum)

number = 10
while number > 0:
    number = number - 1
    if number % 2 == 0:
        continue
    print(number, end=',')
