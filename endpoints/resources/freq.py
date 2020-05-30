from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from endpoints.models.freq import Freq
from app import db
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)

freq_fields = {
    'id_result': fields.Integer,
    'freqword': fields.Integer,
    'count': fields.Integer,
    'word': fields.String,
    'id_text': fields.Integer,
    'time':fields.Integer
}

freq_list_fields = {
    'count': fields.Integer,
    'freqs': fields.List(fields.Nested(freq_fields)),
}

freq_post_parser = reqparse.RequestParser()
freq_post_parser.add_argument('freqword', type=int, required=True, location=['json'],
                              help='freqword parameter is required')
freq_post_parser.add_argument('count', type=int, required=True, location=['json'],
                              help='count parameter is required')
freq_post_parser.add_argument('word', type=str, required=True, location=['json'],
                              help='word parameter is required')
freq_post_parser.add_argument('time', type=int, required=True, location=['json'],
                              help='time parameter is required')
freq_post_parser.add_argument('id_text', type=int, required=True, location=['json'],
                              help='id_text parameter is required')


class FreqResource(Resource):
    @jwt_required
    def get(self, id_result=None):
        if id_result:
            freq = Freq.query.filter_by(id_result=id_result).first()
            return marshal(freq, freq_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            freq = freq.query.filter_by(**args).order_by(freq.id_result)
            if limit:
                freq = freq.limit(limit)

            if offset:
                freq = freq.offset(offset)

            freq = freq.all()
            return marshal({
                'count': len(freq),
                'freqs': [marshal(t, freq_fields) for t in freq]
            }, freq_list_fields)

    @jwt_required
    @marshal_with(freq_fields)
    def post(self):
        args = freq_post_parser.parse_args()

        freq = Freq(**args)
        db.session.add(freq)
        db.session.commit()
        return freq

    @jwt_required
    def put(self, id_result=None):
        return 'method: put, text: frequency'

    @jwt_required
    def delete(self, id_result=None):
        return 'method: delete, text: frequency'
