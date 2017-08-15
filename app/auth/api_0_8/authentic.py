# -*- coding: utf-8 -*-
from .. import auth
from ...models import User
from ...erros.api_0_8 import unauthorized, not_found
from flask import g, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask import current_app


authentic = HTTPBasicAuth()


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


@auth.route('/api_0_8/register', methods=['POST'])
def register():
    """
    @api {post} /api_0_8/register 注册用户
    @apiGroup User
    @qpiVersion 0.8.0
    @apiDescription 请求该接口注册新用户
    @apiParam {string} id 学号
    @apiParam {string} password 密码
    @apiParamExample {json} 测试样例：
     {
       id: 2016212039,
       password: 123456
     }
    @apiSuccess (200) {string} name 用户姓名
    @apiSuccess (200) {string} id 用户id
    @apiSuccessExample {json} 测试样例：
    {
      name: XXX,
      id: 2016212039
    }
    @apiError UserNotFound 用户<code>id</code>或密码错误
    @apiErrorExample {json} 返回样例：
    { error: not found,
      message: id or password is wrong}
    """
    current_app.logger.debug('receive data: id=%s, pw=%s' % (request.values.get('id'),
                             request.values.get('password')))
    user = User.check_user(request.values.get('id'),
                           request.values.get('password'))
    if user is None:
        return not_found('id or password is wrong')
    return jsonify({'name': user.name,
                    'id': user.id})


@auth.route('/api_0_8/token', methods=['GET'])
@authentic.login_required
def get_token():
    """
    @api {get} /api_0_8/token 用户token
    @apiGroup User
    @qpiVersion 0.8.0
    @apiDescription 请求该接口获取用户token,token生存期为两天。<br></br>
    <strong>注意：该接口使用http Basic认证，需要在客户端将用户id和密码进行base64编码并添加当请求头Authorization中</strong>
    @apiSuccess (200) {int} expiration token生存期
    @apiSuccess (200) {timeStamp} timeStamp token生成的时间戳
    @apiSuccessExample {json} 测试样例：
    {
     "expiration": 172800,
     "timeStamp": 1502810538.668,
     "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMjk4MzMzOCwiaWF0IjoxNTAyODEwNTM4fQ.eyJpZCI6MjAxNjIxMjAzOX0.XbzmXyaZyasmvQVHCvr1i3b3otQ7CuC_X7i6t1kWRBY"
    }
    @apiError UserNotFound 用户id或密码错误
    @apiErrorExample {json} 返回样例：
    { error: unauthorized,
      message: unauthorized access}
    """
    return g.user.generate_auth_token()







