#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date    : 2018/8/28 下午2:34
# @Author  : SongXR
# @File    : __init__.py.py
# @Software: PyCharm


"""note:
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from flask_mail import Mail
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 添加路由和自定义错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
