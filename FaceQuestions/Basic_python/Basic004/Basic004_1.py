#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Basic004_1.py
# @Author: HAM
# @File : Basic004_1
"""
计算每一个字母出现的次数
"""
str = 'alafaklasldrsdgla'
#方法一
for i in range(len(str)):
    n = 0
    for j in range(len(str)):
        if str[i] == str[j]:
            n +=1
    print(str[i]+"出现次数为%d"%n)

#方法二
message = "the sdhfdo gdkg agaa g adgdfg"
count  = {}
for c in message:
    count.setdefault(c,0) #如果c不存在，则设置他的值为0
    count[c] = count[c]+1
print(count)

for i in range(len(message)):
   a = message.count(message[i],0,len(message))


#方法三
def count(a):
    a = a
    # 定义一个空字典
    b = {}
    # 求出字符串长度
    c = len(a)
    i = 0
    while i < c:
        # 当定义的字典里有这个字符把他的值加一
        if a[i] in b:
            b[a[i]] += 1
        # 当定义的字典里没有这个字符把这个字符添加到字典里并把他的值设为1
        else:
            b[a[i]] = 1
        i += 1
    # 遍历字典
    for item in b.items():
        print(item)
if __name__ == '__main__':
    count("sfdgdsgfsdvgqewrgfxc")
#
# n = 0
# print(str[1])
# j = 0
# j += 1
# for i in range(len(str)):
#     if str[j] == str[i]:
#         n +=1
#     print(str[j]+"出现了%d次"%n)
