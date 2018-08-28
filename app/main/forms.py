#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 2018/8/28 下午3:23
# @Author  : SongXR
# @File    : forms.py
# @Software: PyCharm

"""note:
"""




from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('您的名字?', validators=[DataRequired()])
    submit = SubmitField('Submit')




