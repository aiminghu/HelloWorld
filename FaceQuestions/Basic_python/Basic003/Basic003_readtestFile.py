#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Basic003_readtestFile.py
# @Author: HAM
# @File : Basic003_readtestFile
'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter filename: ')
print()

#attemt to open file for reading
try:
    fobj = open(fname,'r',encoding='utf-8')

except IOError as e:
    print('*** file open error:',e)
else:
    #display contents to the screen
    for eachLine in fobj:
        print(eachLine) #print语句会自动生成newline
        print(eachLine.strip())#strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    fobj.close()