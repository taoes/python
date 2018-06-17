#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""

import doctest


class Math(object):

    def __init__(self):
        self.number = 12

    def abs(self):

        '''
        if x > 0 return x else return -x
        >>> abs(-1)
        1
        >>> abs(12)
        12
        >>> abs(0)
        0
        '''

        if self.number > 0:
            result = self.number
        else:
            result = -self.number
        return result


if __name__ == '__main__':
    doctest.testmod()
