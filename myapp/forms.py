from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField, SelectField, SelectMultipleField
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

class CardForm(FlaskForm):
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

class DeleteForm(FlaskForm):
    '''
    A form class to remove elements from database.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    delete : SelectField
    submit : SubmitField

    Returns
    -------
    None
    '''
    delete = SelectField('Select')
    submit = SubmitField('Remove')

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

class RenameForm(FlaskForm):
    '''
    A form class to rename files.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    select : SelectField
    submit : SubmitField

    Returns
    -------
    None
    '''

    select = SelectField('Select')
    name = StringField('New Name')
    submit = SubmitField('Rename')

class CardEditForm(FlaskForm):
    '''
    A form class to rename cards.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    select : SelectField
    submit : SubmitField

    Returns
    -------
    None
    '''

    select = SelectField('Select')
    front = StringField('Front')
    back = StringField('Back')
    submit = SubmitField('Rename')

class ShareForm(FlaskForm):
    '''
    A form class to share files to other Users.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    target : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    select = SelectField('Select')
    target = StringField('Target')
    submit = SubmitField('Share')
