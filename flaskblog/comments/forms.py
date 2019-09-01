from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentsForm(FlaskForm):
    title = StringField('Comment..', validators=[DataRequired()])
    submit = SubmitField('Post')