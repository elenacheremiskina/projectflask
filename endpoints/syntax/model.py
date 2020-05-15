from app import db


class Syntax(db.Model):
    __tablename__ = 'syntax'

    id_result = db.Column(db.Integer, primary_key=True, nullable=False)
    id_text = db.Column(db.Integer, db.ForeignKey('text.id_text'), nullable=False)
    comment = db.Column(db.String(1000), nullable=False)

    time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Id: {}, syntax: {}'.format(self.id_result, self.comment)
