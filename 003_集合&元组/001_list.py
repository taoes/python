#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

name_list = ['Tom', 'Jack', 'Smith', 'Mary']
print("name list ", name_list)

# print "Jack" illustrate start index is 0
print("location  is 1 = ", name_list[1])

name_list.append("Anny")
print("name list is = ", name_list)

# print -1 and -2
print("location -1 is", name_list[-1])
print("location -2 is", name_list[-2])

# pop is pop stack

print("pop last", name_list.pop())
print("name list = ", name_list)

# replace
name_list[0] = "new Tom"
print("name list = ",name_list)
