#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lx110.py
# @Author: HAM
# @Date  : lx110

#1.一行代码实现1-100的和
a = sum(range(0,101))
print(a)

#2.在一个函数内部修改全局变量-global关键字
# def fn():
#     global a
#     a = 5
# if __name__ == '__main__':
#     fn()
#     print(a)

#3.Python的标准库
"""
datetime-时间日期
os-提供了与操作系统相关的操作
sys-通常运用于命令行操作
re-正则表达式
math-数学运算

"""
#4.字典如何删除键和合并两个字典
# dic = {"name":"haha","age":20}
# del dic["name"] #删除
# print(dic)
# dic2 = {"name":"niuniu"}
# dic.update(dic2) #合并字典
# print(dic)

#5.谈一下python的GIL（python的全局解释器）

#6.python实现列表去重方法
# a。先通过集合去重，在转列表