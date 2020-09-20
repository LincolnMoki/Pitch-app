from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('product', 'product'), ('sport', 'sport'), ('business', 'business')],
                           validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('leave a comment:', validators=[Required()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you', validators=[Required()])
    submit = SubmitField('Post')
