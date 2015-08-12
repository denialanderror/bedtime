from app import db


class Terms(db.Document):
    category = db.StringField(max_length=12)
    name = db.StringField(max_length=12, unique=True)
    terms = db.ListField(db.StringField(max_length=20))


# Character data
# class Emotion(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(8))
#     term = db.Column(db.String(16), unique=True)


# class Covering(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(8))
#     term = db.Column(db.String(16), unique=True)


# class Name(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(8))
#     term = db.Column(db.String(16), unique=True)


# class Size(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(8))
#     term = db.Column(db.String(16), unique=True)


# class Colour(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     term = db.Column(db.String(16), unique=True)


# class Pattern(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     term = db.Column(db.String(16), unique=True)


# class Kind(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     term = db.Column(db.String(16), unique=True)


# location data
# class Location(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     term = db.Column(db.String(16), unique=True)


# class Mood(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(8))
#     term = db.Column(db.String(16), unique=True)


# Feedback and testing models
# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime)
#     ip = db.Column(db.String(16))
#     story_id = db.Column(db.Integer, unique=True)
#     rating = db.Column(db.Integer)
#     add more here when I've decided what feedback to collect
