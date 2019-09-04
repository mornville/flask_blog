from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),  validators.length(max=30)])
    content = TextAreaField('Content', validators=[DataRequired(),  validators.length(max=400)])
    submit = SubmitField('Post')



class CommentsForm(FlaskForm):
    title = StringField('Comment..', validators=[DataRequired()])
    submit = SubmitField('Post')