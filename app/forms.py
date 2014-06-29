from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required

class PostForm(Form):
    title = TextField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    image = TextField('Image', validators = [Required()])

class EditForm(Form):
    nickname = TextField('Nickname', validators=[Required()])
    email = TextAreaField('Email', validators=[Required()])
    about_me = TextField('About me', validators = [Required()])