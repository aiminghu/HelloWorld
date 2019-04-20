#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Basic003_maketextFile.py
# @Author: HAM
# @File : Basic003
'makeTextFile.py --create text file'
"""
这个脚本提醒用户输入一个（尚不存在的）文件名，然后由用户输入该文件的每一行，最后将文本写入文件.
当文件名存在时，会一直提醒该文件已存在
"""
import os
ls = os.linesep #os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’

fname =input('输入文件名:')
#get filename
while True:
    if os.path.exists(fname): #os.path.模块主要用于文件的属性获取,exists是“存在”的意思，所以顾名思义，os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径
        print("ERROR: %s already exits"%(fname))
    else:
        break
# get file content(text) lines
all = []
print("\nEnter lines（'.' by itself to quit）.\n")

# loop until user terminates input
while True:
    entry = input('请输入文本>')
    if entry == '.':
        break
    else:
        all.append(entry)
# write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print("Done!")