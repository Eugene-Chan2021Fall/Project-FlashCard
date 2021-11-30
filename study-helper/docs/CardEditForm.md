#class CardEditForm(FlaskForm):
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
