#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forChange_01.py
# @Author: HAM
# @File  : forChange_01

"""
if... 条件为真时，执行内部语句，条件为假时，跳出if语句
if... else...
if...elif...else

"""
weather = input('请回答：今晚下雨or没下雨：')
if weather == '下雨':
    print("OK")
answer = input('接受了吗？')
if answer == '接受':
    print('马上举行婚礼')
else:
    print('')