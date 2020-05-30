from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from endpoints.models.syntax import Syntax
from app import db
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)

syntax_fields = {
    'id_result': fields.Integer,
    'id_text': fields.Integer,
    'comment': fields.String,
    'time': fields.Integer
}

syntax_list_fields = {
    'count': fields.Integer,
    'syntaxs': fields.List(fields.Nested(syntax_fields)),
}

syntax_post_parser = reqparse.RequestParser()
syntax_post_parser.add_argument('comment', type=str, required=True, location=['json'],
                              help='comment parameter is required')
syntax_post_parser.add_argument('time', type=int, required=True, location=['json'],
                              help='time parameter is required')
syntax_post_parser.add_argument('id_text', type=int, required=True, location=['json'],
                              help='id_text parameter is required')


class SyntaxResource(Resource):
    @jwt_required
    def get(self, id_result=None):
        if id_result:
            syntax = Syntax.query.filter_by(id_result=id_result).first()
            return marshal(syntax, syntax_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            syntax = syntax.query.filter_by(**args).order_by(syntax.id)
            if limit:
                syntax = syntax.limit(limit)

            if offset:
                syntax = syntax.offset(offset)

            syntax = syntax.all()

            return marshal({
                'count': len(syntax),
                'syntaxs': [marshal(t, syntax_fields) for t in syntax]
            }, syntax_list_fields)
        return 'method: get, text: syntax' 

    @jwt_required
    @marshal_with(syntax_fields)
    def post(self):
        args = syntax_post_parser.parse_args()

        syntax = Syntax(**args)
        db.session.add(syntax)
        db.session.commit()

        return syntax
        return 'method: post, text: syntax' 

    @jwt_required
    def put(self, id_result=None):
        return 'method: put, text: syntax' 

    @jwt_required
    def delete(self, id_result=None):
        return 'method: delete, text: syntax' 
