#class ShareForm(FlaskForm):
    '''
    A form class to share files to other Users.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    select : SelectField
    target : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    select = SelectField('Select')
    target = StringField('Target')
    submit = SubmitField('Share')
