# -*- coding: utf-8 -*-
from .. import auth
from ... import db
from ...models import User
from ...erros.api_0_8 import unauthorized, not_found
from flask import g, request, jsonify
from flask_httpauth import HTTPBasicAuth
from hfut import Student

authentic = HTTPBasicAuth()


@auth.route('/register', methods=['POST'])
def register():
    user = User.check_user(request.values.get('username'),
                           request.values.get('password'))
    if not user:
        return not_found('id or password is wrong')
    return jsonify({'name': user.name,
                    'id': user.id})


@authentic.verify_password
def verify_password(id_or_token, password, campus='hf'):
    user = User.verify_auth_token(id_or_token)
    if not user:
        user = User.check_user(id_or_token, password, campus)
        if not user:
            return False
    g.user = user
    return True


@auth.route('/api_0_8/token', methods=['POST'])
@authentic.login_required
def get_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})



