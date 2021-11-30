#def todo_tracker_delete():
    '''
    This is the route to remove task from the todo-tracker.

    Parameters
    ----------
    GET : /todo-tracker/delete
    POST : delete param
    Returns
    -------
    Renders the todo-tracker_delete.html template.
    Redirects back to /todo-tracker/delete
    '''
    form = DeleteForm()
    list = Task.query.filter_by(author_id = current_user.get_id())
    form.delete.choices = [(g.id, g.task) for g in list]
    if form.validate_on_submit():
        task = Task.query.get(form.delete.data)
        db.session.delete(task)
        db.session.commit()
        flash(f'{task} removed.')
        return redirect('/todo-tracker/delete')

    return render_template("/user/todo-tracker_delete.html", form=form)
