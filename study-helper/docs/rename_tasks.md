#def rename_tasks():
    '''
    This is the route to rename tasks.

    Parameters
    ----------
    GET : /todo-tracker/rename
    POST : rename param, new name
    Returns
    -------
    Renders the todo-tracker/rename.html template.
    Redirects back to /todo-tracker/rename
    '''
    list = Task.query.filter_by(author_id = current_user.get_id())
    form = RenameForm()
    form.select.choices = [(g.id, g.task) for g in list] #Refresh Choices

    if form.validate_on_submit():
        if len(form.name.data) == 0:
            flash('New name is empty.')
        else:
            task = Task.query.get(form.select.data)
            if flashcard is None:
                flash('empty')
            else:
                task.task = form.name.data
                db.session.commit()
                flash('Renaming sucessful')
                form.select.choices = [(g.id, g.task) for g in list] #Refresh Choices
                return redirect('/todo-tracker/rename')
    return render_template("/user/todo-tracker_rename.html", form=form)
