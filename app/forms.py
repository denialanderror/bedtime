from flask.ext.wtf import Form
from wtforms import StringField, SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired, length
from .models import Terms


class CharacterCreator(Form):
    """Validated using WTForms validators to ensure compliance with the parameter requirements
    of database and story generator"""
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
    length = RadioField('length', choices=[('4', 'short'), ('6', 'medium'), ('8', 'long')])


class Feedback(Form):
    """All parameters are optional other than parent_age. Optionality is dealt with in the view method
    and so validation is not required.
    Text fields are validated only for message length to comply with database restrictions"""
    parent_age = IntegerField("reader's age", validators=[DataRequired(u"Please enter your age")])
    child_age = IntegerField("child's age")
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


class Contribute(Form):
    """Allows users to contribute their own texts and phrases (currently only for characters and locations)
    Validated using WTForms validators to ensure compliance with the parameter requirements
    of database and story generator"""
    name_option = SelectField("gender", choices=[('male', 'male'), ('female', 'female')])
    name = StringField('name', validators=[length(max=20, message=u"Please keep to 20 characters")])
    kind_option = SelectField("kind",
                              choices=[(choice, choice) for choice in Terms.objects(category='kind').distinct('name')])
    kind = StringField('kind', validators=[length(max=20, message=u"Please keep to 20 characters")])
    pattern_option = SelectField("pattern", choices=[(choice, choice) for choice in
                                                            Terms.objects(category='pattern').distinct('name')])
    pattern = StringField('pattern', validators=[length(max=20, message=u"Please keep to 20 characters")])
    location_option = SelectField("location", choices=[(choice, choice) for choice in
                                                              Terms.objects(category='location').distinct('name')])
    location = StringField('location', validators=[length(max=20, message=u"Please keep to 20 characters")])
    size_option = SelectField("size",
                              choices=[(choice, choice) for choice in Terms.objects(category='size').distinct('name')])
    size = StringField('size', validators=[length(max=20, message=u"Please keep to 20 characters")])
    covering_option = SelectField("covering", choices=[(choice, choice) for choice in
                                                              Terms.objects(category='covering').distinct('name')])
    covering = StringField('covering', validators=[length(max=20, message=u"Please keep to 20 characters")])
    emotion_option = SelectField("emotion", choices=[(choice, choice) for choice in
                                                            Terms.objects(category='emotion').distinct('name')])
    emotion = StringField('emotion', validators=[length(max=20, message=u"Please keep to 20 characters")])
    mood_option = SelectField("mood",
                              choices=[(choice, choice) for choice in Terms.objects(category='mood').distinct('name')])
    mood = StringField('mood', validators=[length(max=20, message=u"Please keep to 20 characters")])
