#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

name_list = ['tom', 'smith', 'mary']
for name in name_list:
    print("%s" % name)


print("----------------loop print number---------------------")

for i in range(10):
    print(i,end=",")

print("\n----------------loop add number---------------------")
sum = 0
for number in range(101):
    sum = sum + number
print("The sum of 1...100 = " ,sum)