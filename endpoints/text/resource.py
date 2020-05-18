from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Text
from app import db, auth

text_fields = {
    'id_text': fields.Integer,
    'text': fields.String,
    'type': fields.String,
    'file': fields.String
}

text_list_fields = {
    'count': fields.Integer,
    'texts': fields.List(fields.Nested(text_fields)),
}

text_post_parser = reqparse.RequestParser()
text_post_parser.add_argument('text', type=str, required=True, location=['json'],
                              help='text parameter is required')
text_post_parser.add_argument('type', type=str, required=True, location=['json'],
                              help='type parameter is required')
text_post_parser.add_argument('file', type=str, required=True, location=['json'],
                              help='file parameter is required')


class TextResource(Resource):
    @auth.login_required
    def get(self, id_text=None):
        if id_text:
            text = Text.query.filter_by(id_text=id_text).first()
            return marshal(text, text_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            text = text.query.filter_by(**args).order_by(text.id_text)
            if limit:
                text = text.limit(limit)

            if offset:
                text = text.offset(offset)

            text = text.all()

            return marshal({
                'count': len(text),
                'texts': [marshal(t, text_fields) for t in text]
            }, text_list_fields)

    @auth.login_required
    @marshal_with(text_fields)
    def post(self):
        args = text_post_parser.parse_args()

        text = Text(**args)
        db.session.add(text)
        db.session.commit()

        return text

    @auth.login_required
    def put(self, id_text=None):
        return 'method: put, text: text' 
        
    @auth.login_required
    def delete(self, id_text=None):
        return 'method: delete, text: text' 
