from app import db


class Terms(db.Document):
    """Character and location descriptors"""
    category = db.StringField(max_length=12)
    name = db.StringField(max_length=12, unique=True)
    terms = db.ListField(db.StringField(max_length=20))


class ContributeTerms(db.Document):
    """Temporary storage of user contributions before moderation"""
    category = db.StringField(max_length=12)
    name = db.StringField(max_length=12, unique=True)
    terms = db.ListField(db.StringField(max_length=20))


class Texts(db.Document):
    """Story phrases for scenes"""
    category = db.StringField(max_length=20, unique=True)
    texts = db.ListField(db.StringField(max_length=100))


class Actions(db.Document):
    """Phrases related to actions and reactions"""
    category = db.StringField(max_length=20, unique=True)
    action = db.ListField(db.StringField(max_length=100))
    reaction = db.ListField(db.StringField(max_length=100))


class Answers(db.Document):
    """Answers to different types of questions"""
    category = db.StringField(max_length=12)
    answer_type = db.StringField(max_length=12)
    answers = db.ListField(db.StringField(max_length=100))


class Pages(db.EmbeddedDocument):
    """Scenes and their component sentences"""
    page = db.IntField()
    sentences = db.ListField(db.StringField())


class Story(db.Document):
    """Stories and their scenes
    Uses MongoDB internal IDs as UUID for story navigation"""
    title = db.StringField(max_length=70)
    author = db.StringField(max_length=30)
    pages = db.ListField(db.EmbeddedDocumentField(Pages))


class Feedback(db.Document):
    """Stores any feedback from users after story has been read.
    Story ID is obtained to match up feedback and IP address for User analytics.
    Platform and browser obtained for compatibility checking.
    One feedback record per story_id"""
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
    like = db.StringField(max_length=255)
    dislike = db.StringField(max_length=255)
    comments = db.StringField(max_length=255)
