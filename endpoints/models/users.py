from app import db, app
from werkzeug.security import generate_password_hash,  check_password_hash
from flask import Flask, abort, request, jsonify, g, url_for
import time
import jwt
import bcrypt

class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def hash_pass(self, password):
        self.password_hash = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def update(cls, **kwargs):
        print(kwargs.items())
        return {"message": "update"}

    @classmethod
    def get_one_user(cls, email):
        def to_json(item):
            return {
                "id": item.id_user,
                "email": item.email
            }

        user = cls.query.filter_by(email=email).first()

        return {"user": to_json(user)}
