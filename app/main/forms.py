from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')
