from flask.ext.wtf import Form
from wtforms import StringField, SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired, length, optional


class CharacterCreator(Form):
    author = StringField('author', validators=[DataRequired(u"We need this to create the story!"),
                                               length(max=30, message=u"Please keep to 30 characters")])
    hero = StringField('hero', validators=[DataRequired(u"We need this to create the story!"),
                                           length(max=20, message=u"Please keep to 20 characters")])
    # kind = StringField('kind', validators=[DataRequired()])
    kind = StringField('kind')  # might not be used
    gender = RadioField('gender', choices=[('male', 'boy'), ('female', 'girl')],
                        validators=[DataRequired(u"We need this to create the story!")])
    item = StringField('item', validators=[DataRequired(u"We need this to create the story!"),
                                           length(max=20, message=u"Please keep to 20 characters")])


class Feedback(Form):
    parent_age = IntegerField("reader's age", validators=[DataRequired(u"Please enter your age")])
    child_age = IntegerField("child's age", validators=[optional()])
    read_by_child = RadioField('read by child', choices=[(True, "yes"), (False, "no")])
    original = RadioField('original', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    enjoyable = RadioField('enjoyable', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    appropriate = RadioField('appropriate', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    coherent = RadioField('coherent', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    engaging = RadioField('engaging', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    repeat = RadioField('repeat', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    recommend = RadioField('recommend', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    like = StringField("like", validators=[length(max=255, message=u"Please keep to 255 characters")])
    dislike = StringField("dislike", validators=[length(max=255, message=u"Please keep to 255 characters")])
    comments = StringField("comments", validators=[length(max=255, message=u"Please keep to 255 characters")])
