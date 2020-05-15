from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import Semantic
from app import db

semantic_fields = {
    'id_result': fields.Integer,
    'id_text': fields.Integer,
    'comment': fields.String,
    'time': fields.Integer
}

semantic_list_fields = {
    'count': fields.Integer,
    'semantics': fields.List(fields.Nested(semantic_fields)),
}

semantic_post_parser = reqparse.RequestParser()
semantic_post_parser.add_argument('comment', type=str, required=True, location=['json'],
                              help='comment parameter is required')
semantic_post_parser.add_argument('time', type=int, required=True, location=['json'],
                              help='time parameter is required')
semantic_post_parser.add_argument('id_text', type=int, required=True, location=['json'],
                              help='id_text parameter is required')


class SemanticResource(Resource):
    def get(self, id_result=None):
        if id_result:
            semantic = Semantic.query.filter_by(id_result=id_result).first()
            return marshal(semantic, semantic_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            semantic = semantic.query.filter_by(**args).order_by(semantic.id_result)
            if limit:
                semantic = semantic.limit(limit)

            if offset:
                semantic = semantic.offset(offset)

            semantic = semantic.all()

            return marshal({
                'count': len(semantic),
                'semantics': [marshal(t, semantic_fields) for t in semantic]
            }, semantic_list_fields)

    @marshal_with(semantic_fields)
    def post(self):
        args = semantic_post_parser.parse_args()

        semantic = Semantic(**args)
        db.session.add(semantic)
        db.session.commit()

        return semantic

    def put(self, semantic_id=None):
        return 'method: put, text: semantic' 

    def delete(self, semantic_id=None):
        return 'method: delete, text: semantic' 