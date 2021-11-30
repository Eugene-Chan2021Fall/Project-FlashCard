#def rename_sets():
    '''
    This is the route to rename flashcard sets.

    Parameters
    ----------
    GET : /flashcard/rename
    POST : rename param, new name
    Returns
    -------
    Renders the flashcard/rename.html template.
    Redirects back to /flashcard/rename
    '''
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form = RenameForm()
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices

    if form.validate_on_submit():
        if len(form.name.data) == 0:
            flash('New name is empty.')
        else:
            flashcard = Flashcardset.query.get(form.select.data)
            if flashcard is None:
                flash('empty')
            else:
                flashcard.name = form.name.data
                db.session.commit()
                flash('Renaming sucessful')
                form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices
                return redirect('/flashcard/rename')
    return render_template("/flashcard/flashcard_rename.html", form=form)
