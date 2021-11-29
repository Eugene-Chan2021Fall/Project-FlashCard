#class SignupForm(FlaskForm):
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
