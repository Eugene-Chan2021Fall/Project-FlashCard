#class RenderForm(FlaskForm):
    '''
    A form that renders markdown Files.

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
    submit = SubmitField('Render')
