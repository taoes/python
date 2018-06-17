#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

print("ABCDEFG's ASCII 002_编码 :", "ABCDEFG".encode('ascii'))
print("ABCDEFG's UTF-8 002_编码 :", "ABCDEFG".encode('utf-8'))
print("你好's  UTF-8 002_编码:", "你好".encode('utf-8'))

pome = b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa5\xe5\x8f\xaa\xe5\xa6\x82\xe5\x88\x9d\xe8\xa7\x81\xef\xbc\x8c\xe4\xbd\x95\xe4\xba\x8b\xe6\x82\xb2\xe9\xa3\x8e\xe7\xa7\x8b\xe7\x94\xbb\xe6\x89\x87'
print("decode a chinese str : ",pome.decode('utf-8'))
print("人生如之如初见's length = " ,len("人生如之如初见"))