from flask import Flask, jsonify, abort, request, g, url_for
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException, default_exceptions
import urllib
# from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import JWTManager
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

jwt = JWTManager(app)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-JM1M6JLK\SQLEXPRESS;DATABASE=Analysis;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BUNDLE_ERRORS'] = True
app.config['JWT_SECRET_KEY'] = 'jwt-secret'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ["access", "refresh"]
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)

db = SQLAlchemy(app)

from endpoints.models.revoke import RevokedTokenModel
@jwt.token_in_blacklist_loader
def check_token_revoked(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_revoked(jti)

api = Api(app)
api.prefix = '/api'
# auth = HTTPBasicAuth()

# from endpoints.users.resource import UsersResource
# from endpoints.text.resource import TextResource
# from endpoints.syntax.resource import SyntaxResource
# from endpoints.semantic.resource import SemanticResource
# from endpoints.freq.resource import FreqResource
# from endpoints.register.resource import RegisterResource
from endpoints.resources.users import *

# api.add_resource(UsersResource, '/', '/<int:id_user>')

# api.add_resource(TextResource, '/text', '/text/<int:id_text>')
# api.add_resource(SyntaxResource, '/syntax', '/syntax/<int:id_result>')
# api.add_resource(SemanticResource, '/semantic', '/semantic/<int:id_result>')
# api.add_resource(FreqResource, '/freq', '/freq/<int:id_result>')
# api.add_resource(RegisterResource, '/register', '/register/<int:id_text>')

api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserProfile, "/profile")
api.add_resource(LogoutAccess, "/logout/access")
api.add_resource(LogoutRefresh, "/logout/refresh")

if __name__ == '__main__':
    app.run()
