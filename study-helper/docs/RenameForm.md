#class RenameForm(FlaskForm):
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
