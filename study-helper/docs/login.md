#def login():
    '''
    This is the login route endpoint.

    Parameters
    ----------
    GET : /login
    POST : login information

    Returns
    -------
    Renders the login.html template.
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect("/login")
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template("login_templates/login.html", form = form)
