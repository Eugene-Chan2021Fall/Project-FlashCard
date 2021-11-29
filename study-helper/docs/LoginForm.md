#class LoginForm(FlaskForm):
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
