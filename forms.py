from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class UrlForm(FlaskForm):
    url = StringField('Enter a URL to shorten: ', validators=[DataRequired(), URL()])
    submit = SubmitField('Shorten')
