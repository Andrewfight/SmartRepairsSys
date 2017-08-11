# -*- coding: utf-8 -*-
from .. import auth
from ... import db
from ...models import User
from ...erros.api_0_8 import unauthorized, not_found
from flask import g, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask import current_app


authentic = HTTPBasicAuth()


@auth.route('/api_0_8/register', methods=['POST'])
def register():
    current_app.logger.debug('receive data: id=%s, pw=%s' % (request.values.get('id'),
                             request.values.get('password')))
    user = User.check_user(request.values.get('id'),
                           request.values.get('password'))
    if user is None:
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


@authentic.error_handler
def auth_error():
    return unauthorized('unauthorized access')


@auth.route('/api_0_8/token', methods=['POST'])
@authentic.login_required
def get_token():
    return g.user.generate_auth_token()






