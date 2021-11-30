#def flashcard_share():
    '''
    This is the route to share flashcard sets.

    Parameters
    ----------
    GET : /flashcard/rename
    POST : rename param, new name
    Returns
    -------
    Renders the flashcard/rename.html template.
    Redirects back to /flashcard/rename
    '''
    form = ShareForm()
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices

    if form.validate_on_submit:
        checkName = User.query.filter_by(username = form.target.data)
        if checkName is None:
            flash('User not found.')
        elif form.select.data is None:
            flash('Pick a set')
        else:
            flashcard = Flashcardset.query.get(form.select.data)
            share = Flashcardshare(target = form.target.data, flashcard_id = form.select.data, flashcard_name = flashcard.name)
            db.session.add(share)
            db.session.commit()
            flash(f'Flashcard shared to {form.select.data}.')
            flash(f'Flashcard shared to {form.target.data}.')
    return render_template('/flashcard/flashcard_share.html', form=form)
