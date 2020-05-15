from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
# from .model import User
from app import db

class RegisterResource(Resource):
    def get(self):
        return 'method: get, text: register' 

    def post(self):
        return 'method: post, text: register' 

    def put(self):
        return 'method: put, text: register' 

    def delete(self):
        return 'method: delete, text: register' 