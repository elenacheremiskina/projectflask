from app import db


class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id_user, self.name)
