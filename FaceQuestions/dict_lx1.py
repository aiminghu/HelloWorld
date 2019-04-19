#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dict_lx1.py
# @Author: HAM
# @Date  : dict_lx1

"""列表里面套字典"""
# a = [
#     {'id': 1670,  'repoId': 12618, 'uid': 242},
#     {'id': 1667, 'repoId': 0, 'uid': 242},
#     {'id': 1668, 'repoId': 1, 'uid': 242}
#     ]
# b = 0
# print(len(a))
# for i in range(len(a)):
#     if str( a[i]['repoId']) == '12618':
#         print(a[i]['id'])


"""判断字典里的key有没有name字段"""
dicts = {'total': '0', 'createTime': '2019-04-15 10:27:48.352', 'name': 'test', 'updateTime': '2019-04-15 10:27:48.352', 'id': '85', 'status': '1'}
keys = dicts.keys()
print('name' in keys)
# print(keys)