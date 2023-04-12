# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired


class MovieForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = TextAreaField("Enter message here",
                              validators=[InputRequired()])
    poster = FileField('Upload', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField('Submit')