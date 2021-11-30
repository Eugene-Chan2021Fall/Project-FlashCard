#def display():
    '''
    This is the flashcard set route.

    Returns
    -------
    Renders the flashcard_portal.html template.
    '''
    flashcards = Flashcardset.query.filter_by(author_id = current_user.get_id())
    #Getting Share List
    user = User.query.get(current_user.get_id())       #Gets current_user
    share_list = Flashcardshare.query.filter_by(target = user.username)

    return render_template("/flashcard/flashcard_portal.html",
    flashcards = flashcards, share_list = share_list)
