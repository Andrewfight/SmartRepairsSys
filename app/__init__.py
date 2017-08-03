from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name='default'):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app