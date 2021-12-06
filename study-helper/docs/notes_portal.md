#def notes_portal():
    '''
    This is the route to display User's markdown notes.

    Returns
    -------
    Renders the notes_portal.html template.
    '''
    list = Note.query.filter_by(author_id = current_user.get_id())
    user = User.query.get(current_user.get_id())
    shareList = Noteshare.query.filter_by(target = user.username)
    return render_template('notes/notes_portal.html', list=list, shareList=shareList)
