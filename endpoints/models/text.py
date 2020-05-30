from app import db


class Text(db.Model):
    __tablename__ = 'text'

    id_text = db.Column(db.Integer, primary_key=True, nullable=False)
    file = db.Column(db.String(1000), nullable=False)

    def __repr__(self):      
        return 'Id: {}, text: {}'.format(self.id_text, self.file)
