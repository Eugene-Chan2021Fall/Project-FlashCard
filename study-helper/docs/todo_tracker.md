#def todo_tracker():
    '''
    This is the route to display/add to the todo-tracker.

    Parameters
    ----------
    GET : /todo-tracker
    POST : tasks
    Returns
    -------
    Renders the todo-tracker.html template.
    '''
    add_form = TaskForm()
    list = Task.query.filter_by(author_id = current_user.get_id())
    if add_form.validate_on_submit():
        task = Task(task = add_form.task.data, author_id = current_user.get_id())
        db.session.add(task)
        db.session.commit()
        flash('Task added.')

    return render_template("/user/todo-tracker.html", add_form=add_form, list=list)
