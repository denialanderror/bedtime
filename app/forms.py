from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class CharacterCreator(Form):
    author = StringField('author', validators=[DataRequired()])
    hero = StringField('hero', validators=[DataRequired()])
    kind = StringField('kind', validators=[DataRequired()])
    gender = SelectField('gender', choices=[('male', 'He'), ('female', 'She')])
    item = StringField('item', validators=[DataRequired()])
