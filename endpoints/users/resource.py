from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import User
from app import db

user_fields = {
    'id_user': fields.Integer,
    'email': fields.String,
    'surname': fields.String,
    'name': fields.String,
    'patronymic': fields.String,
    'position':fields.String
}

user_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(user_fields)),
}

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('email', type=str, required=True, location=['json'],
                              help='email parameter is required')
user_post_parser.add_argument('surname', type=str, required=True, location=['json'],
                              help='surname parameter is required')
user_post_parser.add_argument('name', type=str, required=True, location=['json'],
                              help='name parameter is required')
user_post_parser.add_argument('patronymic', type=str, required=True, location=['json'],
                              help='patronymic parameter is required')
user_post_parser.add_argument('position', type=str, required=True, location=['json'],
                              help='position parameter is required')


class UsersResource(Resource):
    def get(self, id_user=None):
        if id_user:
            user = User.query.filter_by(id_user=id_user).first()
            return marshal(user, user_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            user = User.query.filter_by(**args).order_by(User.id_user)
            if limit:
                user = user.limit(limit)

            if offset:
                user = user.offset(offset)

            user = user.all()

            return marshal({
                'count': len(user),
                'users': [marshal(u, user_fields) for u in user]
            }, user_list_fields)

    @marshal_with(user_fields)
    def post(self):
        args = user_post_parser.parse_args()

        user = User(**args)
        db.session.add(user)
        db.session.commit()

        return user

    def put(self, id_user=None):
        return 'method: put, text: users' 

    def delete(self, id_user=None):
        return 'method: delete, text: users' 