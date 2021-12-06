#class FileForm(FlaskForm):
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
    name = StringField('Name')
    submit = SubmitField('Upload')
