#class CardForm(FlaskForm):
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
