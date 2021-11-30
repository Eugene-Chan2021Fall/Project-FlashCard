#def logout():
    '''
    This is the logout route endpoint.

    Returns
    -------
    Redirects back to the home directory.
    '''
    logout_user()
    return redirect("/")
