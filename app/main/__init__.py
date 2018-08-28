#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 2018/8/28 下午3:16
# @Author  : SongXR
# @File    : __init__.py.py
# @Software: PyCharm


"""note:
"""

from flask import Blueprint


main = Blueprint('main', __name__)

from . import views, errors