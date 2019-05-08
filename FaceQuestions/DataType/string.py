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
#str.count(sub, start= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
"""
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置
"""
import base64
print(str.count('o',))
#str.encode(encoding='UTF-8',errors='strict')
"""
返回编码后的字符串
encoding -- 要使用的编码，如"UTF-8"
errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值
"""
#在pycharm中，需要先导入base64模块
str1 = "this is string !!"
#str3转成bytes的string
str3 = str1.encode(encoding ='utf-8',errors = 'strict');
print (str3)
print ('')
#bytes再进行base64编码
str4= base64.b64encode(str3)
print (str4)
print ('')
#在base64 decode下
print (str4.decode())
print ('')
# base64解码
enstr = base64.b64decode(str4.decode())
print(enstr.decode())

#str.decode(encoding='UTF-8',errors='strict')
"""
encoding 指定的编码格式解码字符串。默认编码为字符串编码。
返回解码后的字符串
"""

#str.endswith(suffix[, start[, end]])
"""
用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。
"""
a = "hello hello f 好!!!"
print(a.endswith("!!!",0,10))
print(a.endswith('he'))

#str.expandtabs(tabsize=8)
"""
把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8
tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数
str.expandtabs(n) 跟踪每行上的当前光标位置，并将其找到的每个制表符字符替换为当前光标位置到下一个制表位的空格数
"""
#
# str = "hello,I`m\ta man"
# print(str)
# print(str.expandtabs())
# print(str.expandtabs(16))
#
# str = "this is\tstring"
# for i in range(10):
#     print(str.expandtabs(i).replace(' ', "*"), i)
#
# def expandtabs(string, n):
#     result = ""
#     pos = 0
#     for char in string:
#         if char == "\t":
#             # instead of the tab character, append the
#             # number of spaces to the next tab stop
#             char = " " * (n - pos % n)
#         if char == "\n":
#             pos = 0
#         else:
#             pos += len(char)
#         result += char
#     return result
# if __name__ == '__main__':
#     input = "123\t12345\t1234\t1\n12\t1234\t123\t1"
#     print(expandtabs(input, 10))

#str.find(str, beg=0, end=len(string))
# str.rfind(str, beg=0 end=len(string)) 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
"""
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
"""
info = 'acesad'
print(info.find('a',1)) # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3

# str.index(str, beg=0, end=len(string))方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与find()方法一样，只不过如果str不在 string中会报一个异常。
# str.rindex(str, beg=0 end=len(string)) 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
#str.isalnum() 检测字符串是否由字母和数字组成。
"""
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
"""
a = 'hello 123'
b = '12324'
c = 'qweasd'
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print('')
#str.isalpha()检测字符串是否只由字母组成
"""
如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
"""
print(b.isalpha())
print(c.isalpha())

# str.isdecimal() 检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
"""
注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
如果字符串是否只包含十进制字符返回True，否则返回False。
"""

#str.isdigit()检测字符串是否只由数字组成。
print(c.isdigit())
print(c)
# str.islower() 方法检测字符串是否由小写字母组成
# str.isspace()方法检测字符串是否只由空格组成。
#str.istitle()方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
str = "A小米 hello world"
print(str)
print(str.istitle())

#str.isupper()方法检测字符串中所有的字母是否都为大写
print('isuuper方法')
print(str.isupper())
# ★ str.join(sequence)方法用于将序列中的元素以指定的字符连接生成一个新的字符串
"""
返回通过指定字符连接序列中元素后生成的新字符串。
sequence -- 要连接的元素序列
"""
str = "-"
seq = ["xiao", "明天", "beautiful"]# 字符串序列
print (str.join(seq))
#str.ljust(width[, fillchar])方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
# str.rjust(width[, fillchar]) 返回一个原字符串右对齐
# str.zfill(width) 返回指定长度的字符串，原字符串右对齐，前面填充0
"""
width -- 指定字符串长度。
fillchar -- 填充字符，默认为空格。
"""
str = 'this is A string eXample !!'
print(str.ljust(50,'0'))
print("zfill方法右填充%s"%str.zfill(20))
# str.lower()转换字符串中所有大写字符为小写
# str.upper()转换字符串中所有小写字符为大写
# str.swapcase() 对字符串的大小写字母进行转换
print(str.lower())
print("z大小写转换：%s"%str.swapcase())

# str.lstrip([chars])用于截掉字符串左边的空格或指定字符
# str.rstrip([chars])用于截掉字符串右边的空格或指定字符
str = '       hello world!!   '
print(str.lstrip())
str = '222222 hello world!!!222222'
print(str.lstrip('2'))

#maketrans(intab,outtab)maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# str.translate(table[, deletechars]); table -- 翻译表，翻译表是通过maketrans方法转换而来。
# deletechars -- 字符串中要过滤的字符列表。
"""
两个字符串的长度必须相同，为一一对应的关系
intab -- 字符串中要替代的字符组成的字符串。
outtab -- 相应的映射字符的字符串。
供translate()方法使用

"""
intab = 'abcde'
outtab = '12345'
trantab =str.maketrans(intab,outtab)
str = 'today brow consider delete essisive'
print(str.translate(trantab))
# max(str) 返回字符串中最大的字母
# min(str) 返回字符串中最小的字母
print('最大的字母%s'%max(str))

# str.partition(str) 根据指定的分隔符将字符串进行分割
# str.rpartition(str) 方法是从目标字符串的末尾也就是右边开始搜索分割符
"""
如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
"""
str = 'www-baidu.com'
print(str.partition('.'))

# str.replace(old, new[, max]) 符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
"""
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
"""
str = 'today is today!'
print(str.replace('to','TO'))
print(str.replace('to','zzzzzz',1))

# str.split(str="", num=string.count(str))通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
"""
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有
"""
str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str.split())
print(str.split(' '))
print(str.split( ' ',1))

# str.splitlines([keepends]) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
"""
keepends -- 在输出结果里是否保留换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符
返回一个包含各行作为元素的列表
"""

str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())
print(str1.splitlines(True))

# str.startswith(str, beg=0,end=len(string));
"""
用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
str -- 检测的字符串。
strbeg -- 可选参数用于设置字符串检测的起始位置。
strend -- 可选参数用于设置字符串检测的结束位置
"""
str = 'this is an example'
print(str.startswith('this'))
print(str.startswith('is',2,4))

#todo:补充小例子，找面试题