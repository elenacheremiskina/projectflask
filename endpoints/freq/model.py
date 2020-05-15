from app import db


class Freq(db.Model):
    __tablename__ = 'freq'

    id_result = db.Column(db.Integer, primary_key=True)
    freqword = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    word = db.Column(db.String(20), nullable=False)
    id_text = db.Column(db.Integer, db.ForeignKey('text.id_text'), nullable=False)
    time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Id: {}, text: {}'.format(self.id_result, self.freqword)
