#def delete_sets():
    '''
    This is the route to delete flashcard sets.

    Parameters
    ----------
    GET : /flashcard/delete
    POST : delete param
    Returns
    -------
    Renders the flashcard_delete.html template.
    Redirects back to /flashcard/delete
    '''
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form = DeleteForm()
    form.delete.choices = [(g.id, g.name) for g in list]
    if form.validate_on_submit():
        flashcard = Flashcardset.query.get(form.delete.data)
        if flashcard is None:
            flash('empty')
        else:
            db.session.delete(flashcard)
            db.session.commit()
            flash(f'{flashcard} has been removed.')
            return redirect('/flashcard/delete')
    return render_template('/flashcard/flashcard_delete.html', form=form)
