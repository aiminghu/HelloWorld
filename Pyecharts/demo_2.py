#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo_2.py
# @Author: HAM
# @Date  : demo_2
from pyecharts import Bar

bar = Bar("我的第一个图表","这里是副标题")
bar.add("服装", ["P0", "P1", "P2", "P3", "微小"], [65, 177, 177, 4, 0])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render()


