#class FlashcardForm(FlaskForm):
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
