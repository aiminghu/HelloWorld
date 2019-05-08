#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app.py
# @Author: HAM
# @File : app
"""
flask,web微型框架
仅保留核心功能：请求相应处理Werkzeug(WSGI工具库)，模板渲染（Jinja）

"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to my"