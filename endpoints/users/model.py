from app import db, app, auth
from werkzeug.security import generate_password_hash,  check_password_hash
from flask import Flask, abort, request, jsonify, g, url_for
import time
import jwt

class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id_user, self.name)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id_user, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id_user'])

@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
