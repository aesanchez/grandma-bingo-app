from app import db

class PhotoSelection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    photo = db.Column(db.String(40), unique=True, nullable=False)
    number = db.Column(db.Integer)