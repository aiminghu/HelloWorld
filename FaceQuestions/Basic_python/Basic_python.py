#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Basic_python.py
# @Author: HAM
# @File : Basic_python

'''
核心编程 第二版
第三章
3.1 语句和语法
1、井号（#）表示之后的字符为Python注释
2、换行（\n）是标准的行分隔符（通常一个语句一行）
3、反斜杠（\）继续上一行
4、分号（;）将2个语句连接在一行
5、冒号（:）将代码块的头和体分开
6、语句（代码块）用缩进块的方式体现
7、不同的缩进深度分隔不同的代码块
8、Python文件以模块的形式组织 用import导入
'''
# import sys,keyword
#
# #这行是注释
# print("这是换行符\n换行啦")
# a = 1
# b = 0
# if(a == 1) and \
#         (b == 0):
#     print("'\\'是继续下一行")
#
#
#
# print('''
# 三引号下的字符串可以支持多行书写。
# hello
# ''')
# #给一些变量赋值,用括号可以多行
# a , b, c =(2,3,4)
# print(a,b,c)
# #同一行书写多个语句；
# x = 'foo'; sys.stdout.write(x + '\n')

"""
3.2 变量赋值
1、赋值操作符 +，Python中是通过引用来传递的 
2、增量赋值
+= -= *=  /=  %=  **=  <<=  >>=  &=  ^=  |=
3、多重赋值
4、“多元”赋值
"""
# x = 1
# y = x = x + 1
# print(x,y)
#
# x += 1
# print(x)
# z = 5
# z <<= 2
# print(z)
#
# a,b,c = (1,5,"a")
# print(a,b,c)
#
# '''
# python变量交换
# '''
# x,y = 1,2
# print(x,y)
# x,y = y,x
# print(x,y)

"""
3.3 标识符
1、合法的标识符
    a.第一个字符必须是字母或下划线
    b.剩下的字符可以是字母和数字或下划线
    c.大小写敏感
2、关键字
    Keyword模块中，包含一个关键字列表和一个iskeyword()函数
    具体贴图
3、内建（built-in）

4、专用下划线标识符(作为变量前缀或后座指定特殊变量)
    _XXX 不用‘from module import *’ 导入
    _XXX_ 系统定义名字
    _XXX 类中的私有变量名
"""

"""
3.4 基本风格指南
注释：准确，尽量简洁
文档：提供一个机制，通过_doc_变量，动态获得文档字符串
    在模块、类声明或者函数声明中第一个没有赋值的字符串可以用属性obj._doc_来访问，在运行时也可是进行
缩进、选择符标识符名称、Python风格指南
1、模块结构和布局
    A.起始行(unix)，有起始行就能仅输入脚本名字来执行脚本，无需调用解释器
    B.模块文档，简要介绍模块的功能及重要全局变量的含义，模块可通过module.__doc__访问
    C.模块导入
    D.变量定义
    E.类定义
    F.函数定义
    G.主程序
2、在主程序中书写测试代码

"""
# /usr/bin/env python
# "this is a test module"
# import sys,os
#
# debug = True
# class FooClass(object):
#     "Foo class"
#     pass
#
# def test():
#     "test function"
#     foo = FooClass()
#     if debug:
#         print('ran test()')
#
# if __name__ == '__main__':
#     test()

"""
3.5 内存管理
变量无须事先说明
变量无须指定类型
程序员不用关心内存管理
变量名会被“回收”
del语句能够直接释放资源
1、变量定义：变量在第一次赋值时自动声明，赋值后可通过变量名来访问
2、动态类型：python是一种解释型语言，无须声明变量及变量类型。变量在创建（赋值时），解释器会根据语法和右侧的操作数来决定新对象的类型。
在对象创建后，一个该对象的应用会被赋值给左侧的变量
3、内存分配:python解释器会在变量使用后，释放借用的内存
4、引用计数：当对象被创建后，就有一个引用计数，当这个对象不需要时，引用计数变为0时，就会被垃圾回收
    计数增加：对象被创建；另外的别名被创建；被作为参数传递给函数（新的本地引用）；成为容器对象的一个元素
    计数减少：一个本地引用离开了其工作范围，比如函数结束时；对象的别名被显式销毁（del y）;对象的一个别名被赋值给其他对象；
    对象被从一个窗口对象中移除（MyList.remove(x)）;窗口对象本身被销毁
5、垃圾收集
"""
"""
3.7 相关模块和开发工具
《Python风格指南》、《Python快速参考指南》、《Python常见问答》
调试器：pdb
记录器：logging,日志系统，五种级别（紧急、错误、警告、信息、调试）
性能测试器：profile,hotshot,cProfile
"""


"""
4.python对象
1、所有的python对象都拥有三个特性（身份，类型，值）
    a.身份：每个对象都有一个唯一的身份来标识。id()可得到
    b.类型：决定了对象可以保存什么样的值，进行什么样的操作，遵循什么样的规则。type()可知道
    c.值：数据表示的数据项
2、标准类型
    a.数字（Integer整型，Long integer长整型，Floating point real number浮点型,Complex number复数型，Boolean布尔型）
    b.字符串 String 
    c.List 列表
    d.Tuple 元祖
    e.Dictionary 字典
3、其他内建类型：
    a.类型 type()
    b.Null对象（None）  ps：每个对象天生具有布尔值，空对象、值为零的任何数字或者Null对象的None的布尔值都是false
    c.文件 d.集合/固定集合 e.函数/方法 f.模块 g.类

4、python 提供了 is / is not来测试变量是否指向同一个对象
    not,and,or(逻辑非，与，或)
    cmp(o1,o2) 比较o1,o2,根据比较结果返回整型,python3中用operator模块代替
    str(o1) 转换成字符串类型
    type(o1) 得到o1的数据类型
    repr(o1) 转成字符串，一般可用eval()内建函数得到原来的对象
5、类型工厂函数
    dict(),bool(),set(),frozenset()
    object(),classmethod()
    super(),property(),file() .....

6、存储模型：字典、元祖、列表=容器类型；数字、字符串=标量/原子类型
7、更新模型：字典、列表 = 可变类型；数字、字符串、元祖=不可变类型
8、访问模型：数字=直接访问；字符串、列表、元祖 = 顺序访问；字典 = 映射访问
    
"""
# foo1 = foo2 = 4.3 #指向同一个
# fo1 = 4.3
# fo2 = fo1
#
# f1 = 4.4 #指向不同的
# f2 = 2.2 + 2.2
#
# print(f1 is f2) #false,
# print(fo1 is fo2)#true
# print(type(str(f1)))
#
# a = 10
# b = 10
# c = 100
# d = 100
# e = 10.0
# f = 10.0
# print(a is b)
# print(c is d)
# print(e is f)

"""
5.数字 
"""