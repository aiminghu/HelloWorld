#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : typechk.py
# @Author: HAM
# @File : typechk
"""
检查类型
"""
import types

def displayNumType(num):
    print(num,'is')
    if isinstance(num,(int,float,complex)):
        print('a number of type:',type(num).__name__)
    else:
        print('not a number at all!')

def displayNumType_1(num):#需要考虑性能
    print(num, 'is')
    if type(num) == type(0):
        print('an integer')
    elif type(num) == type(0.0):
        print('a float')
    elif type(num) == type(0+0j):
        print('a complex number')
    else:
        print('not a number')


if __name__ == '__main__':
    displayNumType_1(-69)
    displayNumType_1(999999999999999999)
    displayNumType_1(98.9)
    displayNumType_1(-5.2+1.9j)
    displayNumType_1('xx')