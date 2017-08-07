# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import logging
import logging.config
import logging.handlers
import os
import sys


db = SQLAlchemy()


def create_app(config_name='default'):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app

# 配置文件报错
# config_file = '%s/logging.conf' % os.path.dirname(os.path.realpath(__file__))
# config_file = 'C:\\Users\\AllenShen\\Documents\\projects\\Python Projects\\SmartRepairsSystem\\app\\logging.conf'
# logging.config.fileConfig(config_file)

'''
def get_logger(name, level='INFO', handlers=None, formatter=None):
    # 使用时自定义handler类型，通过该函数获取将handler传入完成组装获得logger对象
    logging.basicConfig()
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if handlers is None:
        handlers = [logging.StreamHandler(sys.stdout)]
    if formatter is None:
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatter)
    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

file_handler = logging.handlers.TimedRotatingFileHandler('../log/', when='D',
                                                         interval=1, backupCount=10)
file_handler.suffix = '%Y-%m-%d.log'
handlers = []
handlers.append(file_handler)
root_logger = get_logger('my_root', 'DEBUG', handlers)
root_logger.debug('root logger generated')
'''