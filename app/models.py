from app import db


class Terms(db.Document):
    category = db.StringField(max_length=12)
    name = db.StringField(max_length=12, unique=True)
    terms = db.ListField(db.StringField(max_length=20))


class Texts(db.Document):
    category = db.StringField(max_length=20, unique=True)
    texts = db.ListField(db.StringField(max_length=70))


class Actions(db.Document):
    category = db.StringField(max_length=20, unique=True)
    actions = db.ListField(db.StringField(max_length=70))
    reactions = db.ListField(db.StringField(max_length=70))


class Pages(db.EmbeddedDocument):
    page = db.IntField()
    sentences = db.ListField(db.StringField())


class Story(db.Document):
    pages = db.ListField(db.EmbeddedDocumentField(Pages))


class Feedback(db.Document):
    story_id = db.IntField(unique=True)
    ip = db.StringField()
    platform = db.StringField()
    browser = db.StringField()
    rating = db.IntField()
    parent_age = db.IntField()
    child_age = db.IntField()
    read_by_child = db.BooleanField()
    original = db.IntField()
    enjoyable = db.IntField()
    appropriate = db.IntField()
    coherent = db.IntField()
    engaging = db.IntField()
    repeat = db.IntField()
    recommend = db.IntField()
    like = db.StringField()
    dislike = db.StringField()
    comments = db.StringField()
