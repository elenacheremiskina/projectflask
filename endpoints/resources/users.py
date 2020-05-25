from flask_restful import Resource, reqparse, request, fields, marshal_with, marshal
from flask import Flask, abort, request, jsonify, g, url_for
from endpoints.models.users import User
from app import db

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)
from flask import request
from werkzeug.utils import secure_filename

from endpoints.models.users import User
from endpoints.models.revoke import RevokedTokenModel

parser = reqparse.RequestParser()


user_fields = {
    'id_user': fields.Integer,
    'email': fields.String,
    'surname': fields.String,
    'name': fields.String,
    'patronymic': fields.String,
    'position': fields.String,
    'password_hash': fields.String
}

user_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(user_fields)),
}

class UserRegister(Resource):
    def post(self):
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
        user_post_parser.add_argument('password_hash', type=str, required=True, location=['json'],
                              help='password_hash parameter is required')
        
        email = request.json.get('email')
        password = request.json.get('password_hash')
        args = user_post_parser.parse_args()

        user = User(**args)
        user.hash_pass(password)

        user.save_to_db()
        access_token = create_access_token(identity=args["email"])
        refresh_token = create_refresh_token(identity=args["email"])

        return {
            "message": "Register success",
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        

class UserLogin(Resource):
    def post(self):
        user_post_parser = reqparse.RequestParser()
        user_post_parser.add_argument('email', type=str, required=True, location=['json'],
                                      help='email parameter is required')
        user_post_parser.add_argument('password_hash', type=str, required=True, location=['json'],
                                      help='password_hash parameter is required')
        email = request.json.get('email')
        password_hash = request.json.get('password_hash')
        args = user_post_parser.parse_args()

        user = User(**args)

        current_user = User.find_by_email(args["email"])

        if not current_user:
            return error.DOES_NOT_EXIST

        if not current_user.check_pass(password_hash):
            return error.WRONG_PASSWORD

        access_token = create_access_token(identity=current_user.email)
        refresh_token = create_refresh_token(identity=current_user.email)

        return {
            "message": "Login success",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "password": args["password_hash"],
            "pass":current_user.password_hash,
            "password_hash": password_hash,
        }


class UserProfile(Resource):
    @jwt_required
    def put(self):
        return {"message": "upload"}

    @jwt_required
    def get(self):
        print(request.headers)
        email = get_jwt_identity()
        return User.get_one_user(str(email))

    @jwt_required
    def post(self):
        return {"message": "post"}


class LogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()

            return {"message": "Token has been revoked"}
        except Exception as e:
            print(e)

            return {"message": "Something went wrong"}


class LogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()

            return {"message": "Refresh token has been revoked"}
        except Exception as e:
            print(e)

            return {"message": "Some thing went wrong"}
