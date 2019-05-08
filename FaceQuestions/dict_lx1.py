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
# dicts = {'total': '0', 'createTime': '2019-04-15 10:27:48.352', 'name': 'test', 'updateTime': '2019-04-15 10:27:48.352', 'id': '85', 'status': '1'}
# keys = dicts.keys()
# print('name' in keys)
# # print(keys)
"""
把name的值放入列表中，判断列表的首字母是否包含zh开头
"""
# list = [{'displayRealName': 'zhengxiaojun', 'avatarUrl': 'http://172.17.6.31:7350/v0101/Y4xvo43io450o4kiM2wio4WdMJA0Y2OxpaAio_5joyp', 'name': 'zhengxiaojun', 'id': '276'}, {'displayRealName': 'zhangqingxun', 'avatarUrl': 'http://172.17.6.31:7350/v0101/Y4xvo43io450o4kiM2wio4WdMJA0Y2OxpaAio_5joyp', 'name': 'zhangqingxun', 'id': '332'}, {'displayRealName': 'zhangwei', 'avatarUrl': 'http://172.17.6.31:7350/v0101/Y4xvo43io450o4kiM2wio4WdMJA0Y2OxpaAio_5joyp', 'name': 'zhangwei', 'id': '341'}, {'displayRealName': 'zhaofei', 'avatarUrl': 'http://172.17.6.31:7350/v0101/Y4xvo43io450o4kiM2wio4WdMJA0Y2OxpaAio_5joyp', 'name': 'zhaofei', 'id': '356'}]
# name = []
# for i in range(len(list)):
#     if list[i]['name'] not in name:
#         name.append(list[i]['name'])
# print(name)
# for i in range(len(name)):
#     print(name[i].startswith('zh',0,2))


dict = {'pageIndex': 1, 'pageSize': 20, 'totalPage': 1, 'totalRowCount': 2, 'ts': 0, 'modelList': [{'createTime': '2019-04-15 11:38:12.0', 'name': 'name', 'updateTime': '2019-04-15 11:38:12.0', 'id': '87', 'url': '/user/zhizi/resource/folder/242/87/rowKeyList'}, {'createTime': '2019-04-15 10:27:48.0', 'name': 'test', 'updateTime': '2019-04-15 10:27:48.0', 'id': '85', 'url': '/user/zhizi/resource/folder/242/85/rowKeyList'}]}
list = [{'createTime': '2019-04-15 11:38:12.0', 'name': 'name', 'updateTime': '2019-04-15 11:38:12.0', 'id': '87', 'url': '/user/zhizi/resource/folder/242/87/rowKeyList'}, {'createTime': '2019-04-15 10:27:48.0', 'name': 'test', 'updateTime': '2019-04-15 10:27:48.0', 'id': '85', 'url': '/user/zhizi/resource/folder/242/85/rowKeyList'}]

print(list)
print(list[0]['name'])
print(len(dict['modelList']))
print(dict['modelList'][0]['createTime'])