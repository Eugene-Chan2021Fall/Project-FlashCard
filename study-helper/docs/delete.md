#def delete():
    '''
    This is the delete route endpoint.

    Returns
    -------
    Redirects back to the home directory.
    '''
    user = User.query.get(current_user.get_id())
    logout_user()
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.username} has been deleted.')
    return redirect("/")
