#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : string.py
# @Author: HAM
# @File : str
"""
字符串的用法
"""
var1 = "Hello World!"
var2 = "Python Runoob"

#通过方括号来访问
print('var1[0]:'+var1[0])
print('var2[1:5]:'+var2[1:5])

#更新字符串
print("更新字符串",var1[:6]+"Python")

#字符串运算
a = 'hello'
b = 'python'
print("+可以连接字符串a+b:",a+b)
print("*可以重复输出字符串a*3:",a*3)
print("[]可以通过索引获取字符串中字符a[0]:",a[0])
print("[:]可以截取字符串中的一部分a[1:4]",a[1:4])
#成员运算符in / not in
print("in字符串包含给定的字符返回True",'o' in a)
print("not in字符串不包含给定的字符返回True",'o' not in a)
#字符串格式化 %, format()
print("我的名字是%s,年龄是%d岁"%('Lily',18))
print("{} {}".format("hello","world")) #不指定位置，按默认程序
print("{0} {1} {0}".format("hello","world"))#设置指定位置

print("网站名：{name}, 地址 {url}".format(name="百度", url="www.baidu.com"))
#通过字典设置参数
site = {"name":"百度","url":"www.baidu.com"}
print("网站名：{name}, 地址 {url}".format(**site))
#通过列表索引设置参数
my_list = ['百度','www.baidu.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))

#数字格式化
print("{:.2f}".format(3.1415926)) #保留小数点后两位
print("{:+.2f}".format(3.1415926))#带符号保留小数点后两位
print("{:.0f}".format(3.1415926)) #不保留小数
print("{:0>2d}".format(5)) #数字补零 (填充左边, 宽度为2)
print("{:x<4d}".format(5)) #数字补x (填充右边, 宽度为4)
print("{:x<4d}".format(10))
print("{:,}".format(10000000)) #以逗号分隔的数字形式
print("{:.2%}".format(0.32)) #百分比格式
print("{:.2e}".format(10000000)) #指数记法
print("{:10d}".format(10)) #右对齐 (默认, 宽度为10)
print("{:<10d}".format(10)) #左对齐 (宽度为10)
print("{:^10d}".format(10)) #中间对齐 (宽度为10)

#字符串的内建函数
str = "hello World"
#str.capitalize() 字符串第一个字符大写，其他字母小写
print("把字符串第一个字符大写，其他字母小写",str.capitalize())
#str.(width,'fillchar') 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(str.center(25,'*'))
print(str.center(20))
