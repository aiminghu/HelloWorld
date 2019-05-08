#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list.py
# @Author: HAM
# @File : list
"""
列表
属于序列，可以进行：索引，切片，加，乘，检查成员
列表序列不需要列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
"""
#创建
list1 = []
list2 = ['hello',0,1,2,3,4,5,6,'a']
#访问列表的值
print('用下标索引访问：',list2[0])
print('切片方式访问：',list2[1:5])
# 更新列表
list = []
list.append('a') #添加列表项
print('增加列表项：',list)
list[0] = 'b'
print('修改列表值：',list)
#删除列表元素
print('列表2的内容：',list2)
del list2[2]
print('删除列表下标为2的元素：',list2)

#列表操作符
#与字符串相似  +号用于组合列表，*号用于重复列表
"""
常用
len()  列表元素个数
+  组合列表
*  重复列表
in  判断元素是否存在于列表中
for  in 迭代
"""
a = [1,2,3]
b = [4,'a',6]
print('长度',len(a))
print('组合',a+b)
print('判断元素是否在列表中',3 in a)
for i in a:print('迭代输出',i,end="") #end =''不换行
print("\n****************")

#列表的截取与拼接
L = ['a','b','c']
print('获取第三个元素：',L[2])
print('获取倒数第二个元素，即从右向左',L[-2])
print('获取从第二个元素开始后的所有元素',L[1:])

#嵌套列表
c = [a,b]
print("嵌套列表",c)
print('输出嵌套列表的第一个',c[0])
print("输出其中的元素",c[0][0])

#列表的函数和方法
"""
函数：
    len(list)列表元素个数
    max(list)返回列表元素最大值
    min(list)返回列表元素最小值
    list(seq)将字符串或者元祖转换成列表
方法：
    list.append(obj) 在列表末尾添加新的对象.##无返回值，但是会改变原来的列表
    list.count(obj) 统计某个元素在列表中出现的次数
    list.extend(seq) 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.index(obj) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
(从列表中找出某个值第一个匹配项的索引位置)
    list.index(index,obj) 将对象插入列表
    list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj) 移除列表中某个值的第一个匹配项
    list.reverse() 反向列表中元素
    list.sort(cmp=None, key=None, reverse=False)对列表进行排序
    #cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
    #key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    #reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""
aList = [123,'abc','zara']
a = [567,34,'hello']

# print(aList.append("123"))
# print(aList)
# print(aList.append(a))
# print(aList)
print("###################")
aList.extend(a) #将两个列表合并
print(aList)
print("index()输出找的对象的索引位置：",aList.index(123))
print("移除列表中的数，默认最后一个",aList.pop())
print(aList)
print(aList.remove(34))
print("remove删除后的第一个数：",aList)
aList.reverse()
print("反向列表内容",aList)
print("************************")
bList = ['google','hello','taobao','baidu']
print(bList)
bList.sort() #字符串和数字不能做比较
print("排序后的列表：",bList)
#降序
bList.sort(reverse=True)
print("降序输出后的列表：",bList)
#指定列表中的元素排序来输出列表

def takeSecond(elem):
    return elem[1]

random = [(2,2),(4,1),(3,4),(1,3)]
print("helo",takeSecond(random))
random.sort(key=takeSecond)

print('排序列表：',random)


if __name__ == '__main__':
    random = [(2, 2), (4, 1), (3, 4), (1, 3)]
    print(takeSecond(random))
