#class DeleteForm(FlaskForm):
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
