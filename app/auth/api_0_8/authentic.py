from .. import auth
from ... import db
from ...models import User
from flask_httpauth import HTTPBasicAuth
from ...erros.api_0_8 import unauthorized
from hfut import Student

authentic = HTTPBasicAuth()

@authentic.verify_password
def verify_password(id, password):

