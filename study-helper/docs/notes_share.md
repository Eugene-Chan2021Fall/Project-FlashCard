#def notes_share():
    '''
    This is the route allows Users to share notes to other users.

    GET : /notes/share
    POST : Note

    Returns
    -------
    Renders the notes_share.html template.
    '''

    form = ShareForm()
    list = Note.query.filter_by(author_id = current_user.get_id())
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices

    if form.validate_on_submit:
        checkName = User.query.filter_by(username = form.target.data)
        if checkName is None:
            flash('User not found.')
        elif form.select.data is None:
            flash('Pick a set')
        else:
            note = Note.query.get(form.select.data)
            share = Noteshare(target = form.target.data, note_id = form.select.data, note_name = note.name)
            db.session.add(share)
            db.session.commit()
            flash(f'Flashcard shared to {form.select.data}.')
            flash(f'Flashcard shared to {form.target.data}.')

    return render_template('notes/notes_share.html', form=form)
