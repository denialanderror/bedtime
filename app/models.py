from app import db


class Terms(db.Document):
    category = db.StringField(max_length=12)
    name = db.StringField(max_length=12, unique=True)
    terms = db.ListField(db.StringField(max_length=20))


class Texts(db.Document):
    category = db.StringField(max_length=20, unique=True)
    texts = db.ListField(db.StringField(max_length=70))