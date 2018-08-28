#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 2018/8/28 下午3:17
# @Author  : SongXR
# @File    : views.py
# @Software: PyCharm


"""note:
"""


from flask import render_template, session, redirect, url_for

from datetime import datetime
from . import main
from .forms import NameForm
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('main.index'))
    return render_template('index.html',form = form, name=session.get('name'), current_time=datetime.utcnow())