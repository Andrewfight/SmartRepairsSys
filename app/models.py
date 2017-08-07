# -*- coding: utf-8 -*-
from . import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import hfut.exception
from hfut import Student
import time

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    pw_hash = db.Column(db.String)
    name = db.Column(db.String)
    phone = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    area = db.Column(db.Integer)
    service = db.relationship('Task', backref='user')
    freetime = db.Column(db.PickleType)

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name

    @property
    def __repr__(self):
         return '<User %r>' % self.name

    @property
    def password(self):
        return "cleartext passwords is not accessible"

    @password.setter
    def password(self, password):
        self.pw_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def generate_auth_token(self, expiration=172800):
        # token有效期2天
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        generate_time = time.time()
        token = s.dumps({'id': self.id})
        return jsonify({'token': token.decode('ascii'),
                        'timeStamp': generate_time,
                        'expiration': expiration})

    @staticmethod
    def check_user(id_, password, campus='hf'):
        stu = Student(id_, password, campus)
        current_app.logger.debug('%s,%s' % (id_, password))
        try:
            info = stu.get_my_info()
        except hfut.exception.SystemLoginFailed, e:
            current_app.logger.debug(e)
            return None
        try:
            user = User.query.filter_by(id=id_).first()
            if user is None:
                current_app.logger.debug('id %s does not exist' % id_)
                user = User(id_, password, info[u'姓名'])
                db.session.add(user)
                db.session.commit()
                current_app.logger.debug('id %s insert to db successfully' % id_)
        except Exception, e:
            current_app.logger.debug(e)
            return None
        return user

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])


class Worker(db.Model):
    __tablename__ = 'worker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    area_in_duty = db.Column(db.PickleType)
    tasks = db.relationship('Task', backref='worker')
    worktime = db.Column(db.PickleType)
    arranged = db.Column(db.PickleType)

    def __repr__(self):
        return '<Worker %r>' % self.name


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer)
    task_type = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    submit_time = db.Column(db.DateTime)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    details = db.Column(db.Text)
    change_log = db.Column(db.PickleType)
    is_push = db.Column(db.Boolean)
    change_push = db.Column(db.Boolean)


class Notice(db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('admin.id'))
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, nullable=False)
    authority = db.Column(db.Integer)    
