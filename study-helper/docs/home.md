#def home():
    '''
    This is the home route endpoint.

    Returns
    -------
    Renders the home.html template.
    '''
    if current_user.is_authenticated:
        name = User.query.get(current_user.get_id()).username

        return render_template("user/user_home.html", name = name)
    return render_template("home.html")
