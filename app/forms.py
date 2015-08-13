from flask.ext.wtf import Form
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired


class CharacterCreator(Form):
    author = StringField('author', validators=[DataRequired()])
    hero = StringField('hero', validators=[DataRequired()])
    # kind = StringField('kind', validators=[DataRequired()])
    kind = StringField('kind')
    gender = RadioField('gender', choices=[('male', 'boy'), ('female', 'girl')])
    item = StringField('item', validators=[DataRequired()])


class Rating(Form):
    rating = RadioField('rating', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])