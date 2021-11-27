from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Sign up')
class FlashcardForm(FlaskForm):
    name = StringField('Set Name', validators=[DataRequired()])
    submit = SubmitField('Add Set')
class FlashcardAddForm(FlaskForm):
    front = StringField('Front', validators=[DataRequired()])
    back = StringField('Back', validators=[DataRequired()])
    submit = SubmitField('Add Card')
class FlashcardDeleteForm(FlaskForm):
    front = StringField('Front', validators=[DataRequired()])
    back = StringField('Back', validators=[DataRequired()])
    submit = SubmitField('Remove Card')
