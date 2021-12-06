#def notes_add():
    '''
    This is the route to add Markdown file notes to the database.

    GET : /notes/adds
    POST : File data

    Returns
    -------
    Renders the notes_add.html template.
    '''

    form = FileForm()
    if form.validate_on_submit():
        if len(form.name.data) == 0:
            flash('Empty name')
        else:
            text = form.file.data.read()
            newtext = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
            n = Note(note = text, author_id = current_user.get_id(), name = form.name.data)
            db.session.add(n)
            db.session.commit()


    return render_template('notes/notes_add.html', form=form)
