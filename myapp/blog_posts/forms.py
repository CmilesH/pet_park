from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Link')
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')

