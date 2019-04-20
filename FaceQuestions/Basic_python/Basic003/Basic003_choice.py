#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Basic003_choice.py
# @Author: HAM
# @File : Basic003_choice

import os
def makefile():
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

def readfile():
    fname = input('Enter filename: ')
    print()

    # attemt to open file for reading
    try:
        fobj = open(fname, 'r', encoding='utf-8')

    except IOError as e:
        print('*** file open error:', e)
    else:
        # display contents to the screen
        for eachLine in fobj:
            print(eachLine)  # print语句会自动生成newline
            print(eachLine.strip())  # strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        fobj.close()
def openfile():
    fname = input("输入要编辑的文件名字：")
    with open(fname,'r+',encoding='utf-8') as f:
        line = input("请输入要编辑的内容：")
        f.write(line)


if __name__ == '__main__':
    a = input('请输入你想执行的程序：1 or 2：')
    if int(a) == 1:
        makefile()
    elif int(a) == 2:
        readfile()
    else:
        openfile()
