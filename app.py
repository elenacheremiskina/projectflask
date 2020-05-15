from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import settings

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

import urllib
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-JM1M6JLK\SQLEXPRESS;DATABASE=Analysis;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

db = SQLAlchemy(app)
api = Api(app)
api.prefix = '/api'


from endpoints.users.resource import UsersResource
from endpoints.text.resource import TextResource
from endpoints.syntax.resource import SyntaxResource
from endpoints.semantic.resource import SemanticResource
from endpoints.freq.resource import FreqResource
from endpoints.register.resource import RegisterResource

api.add_resource(UsersResource, '/', '/<int:id_user>')
api.add_resource(TextResource, '/text', '/text/<int:id_text>')
api.add_resource(SyntaxResource, '/syntax', '/syntax/<int:id_result>')
api.add_resource(SemanticResource, '/semantic', '/semantic/<int:id_result>')
api.add_resource(FreqResource, '/freq', '/freq/<int:id_result>')
api.add_resource(RegisterResource, '/register', '/register/<int:id_text>')

if __name__ == '__main__':
    app.run()
