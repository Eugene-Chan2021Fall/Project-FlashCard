#class TaskForm(FlaskForm):
    '''
    A form class to add Tasks to the todo-tracker.

    Parameters
    ----------
    FlaskForm : WTForm

    Fields
    ------
    task : StringField
    submit : SubmitField

    Returns
    -------
    None
    '''
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
