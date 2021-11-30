#def signup():
    '''
    This is the signup route endpoint.

    Parameters
    ----------
    GET : /signup
    POST : signup information

    Returns
    -------
    Renders the signup.html template.
    '''
    form = SignupForm()
    if form.validate_on_submit():
        checkName = User.query.filter_by(username = form.username.data).first()
        checkEmail = User.query.filter_by(email = form.email.data).first()
        if checkName is not None:
            flash('Username already taken')
        elif checkEmail is not None:
            flash('Email already in use')
        else:
            user = User(username = form.username.data, email = form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            #Initalize Time studied
            hour_tracker = HoursTracked(time = 0, author_id = user.id)
            db.session.add(hour_tracker)
            db.session.commit()
            flash('Registration successful')
    return render_template("login_templates/signup.html", form = form)
