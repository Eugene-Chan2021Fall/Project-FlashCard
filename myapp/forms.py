from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    '''
    A class representing a Login Form.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    username : StringField
    password : StringField
    remember_me : BooleanField
    submit : SubmitField

    Returns
    -------
    None
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
class SignupForm(FlaskForm):
    '''
    A class representing a Sign Up Form.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    username : StringField
    email : StringField
    password : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Sign up')
class FlashcardForm(FlaskForm):
    '''
    A form class to make Flashcard Sets.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    name : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    name = StringField('Set Name', validators=[DataRequired()])
    submit = SubmitField('Add Set')
class FlashcardDeleteForm(FlaskForm):
    '''
    A form class to delete Flashcard Sets.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    delete : IntegerField
    submit : SubmitField

    Returns
    -------
    None
    '''
    delete = IntegerField('Delete')
    submit = SubmitField('Delete Set')
class CardAddForm(FlaskForm):
    '''
    A form class to add Cards to FlashCard Sets.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    front : StringField
    back : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    front = StringField('Front', validators=[DataRequired()])
    back = StringField('Back', validators=[DataRequired()])
    submit = SubmitField('Add Card')
class CardDeleteForm(FlaskForm):
    '''
    A form class to delete Cards to FlashCard Sets.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    delete : IntegerField
    submit : SubmitField

    Returns
    -------
    None
    '''
    delete = IntegerField('Delete')
    submit = SubmitField('Remove Card')

class TaskForm(FlaskForm):
    '''
    A form class to add Tasks to the todo-tracker.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    task : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

class TaskDeleteForm(FlaskForm):
    '''
    A form class to remove Tasks to the todo-tracker.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    delete : IntegerField
    submit : SubmitField

    Returns
    -------
    None
    '''
    delete = IntegerField('Delete')
    del_submit = SubmitField('Remove Task')

class FileForm(FlaskForm):
    '''
    A form class upload files to Flashcard Sets.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    file : FileField
    submit : SubmitField

    Returns
    -------
    None
    '''
    file = FileField('File')
    submit = SubmitField('Upload')
