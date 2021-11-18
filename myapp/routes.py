from myapp import myapp_obj
from myapp.forms import LoginForm, SignupForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/")
def home():
    return render_template("home.html")

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect("/login")
        else:
            login_user(user, remember=form.remember_me.data)
            flash(f'Welcome {user.username}!')
            return redirect("/")
    return render_template("login.html", form = form)

@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data,
                password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{user} added to the database.')
    return render_template("signup.html", form = form)
