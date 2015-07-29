from app import database as d

class Character(d.Model):
    id = d.Column(d.Integer, primary_key=True)


class Character_description(d.Model):
    id = d.Column(d.Integer, primary_key=True),
    size = d.Column(d.String)

class Size(d.Model):
    id = d.Column(d.Integer, primary_key=True),
    size = d.Column(d.String),
    descriptor = d.Column(d.String)
