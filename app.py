from flask import Flask, jsonify, abort, request, g, url_for
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException, default_exceptions
import urllib
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

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

db = SQLAlchemy(app)
api = Api(app)
api.prefix = '/api'
auth = HTTPBasicAuth()

from endpoints.users.resource import UsersResource
from endpoints.text.resource import TextResource
from endpoints.syntax.resource import SyntaxResource
from endpoints.semantic.resource import SemanticResource
from endpoints.freq.resource import FreqResource
from endpoints.register.resource import RegisterResource

api.add_resource(UsersResource, '/', '/<int:id_user>')

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.email})

api.add_resource(TextResource, '/text', '/text/<int:id_text>')
api.add_resource(SyntaxResource, '/syntax', '/syntax/<int:id_result>')
api.add_resource(SemanticResource, '/semantic', '/semantic/<int:id_result>')
api.add_resource(FreqResource, '/freq', '/freq/<int:id_result>')
api.add_resource(RegisterResource, '/register', '/register/<int:id_text>')

if __name__ == '__main__':
    app.run(debug=True)
