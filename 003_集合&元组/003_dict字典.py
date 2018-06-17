#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

gradle = {"tom": 100, "tao": 99, "ying": 101}

print("ying's gradle = ", gradle.get("ying"))
print("li in gradle = ","li" in gradle)
print("li's gradle = ", gradle.get("li","Not Found"))

