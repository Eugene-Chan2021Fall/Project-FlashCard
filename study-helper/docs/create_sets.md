#def create_sets():
    '''
    This is the route to create flashcard sets.

    Parameters
    ----------
    GET : /flashcard/create
    POST : new Flashcardset data
    Returns
    -------
    Renders the flashcard_create.html template.
    '''
    form = FlashcardForm()
    user = current_user.get_id()
    flash(f'Debug User Id: {user}')
    if form.validate_on_submit():
        set = Flashcardset(name = form.name.data, author_id = current_user.get_id())
        db.session.add(set)
        db.session.commit()
        return redirect(url_for('flashcard', option="display", name=set.name, id=set.id))
    return render_template("/flashcard/flashcard_create.html", form = form)
