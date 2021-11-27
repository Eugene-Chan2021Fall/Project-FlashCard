from myapp import myapp_obj, pdf
from myapp.forms import LoginForm, SignupForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User
from flask_login import current_user, login_user, logout_user, login_required

from myapp.pomodoro import PomodoroTimer

@myapp_obj.route("/")
def home():
    if current_user.is_authenticated:
        name = User.query.get(current_user.get_id()).username
        return render_template("user_home.html", name = name)
    return render_template("home.html")

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect("/login")
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template("login.html", form = form)

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signup():
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
            flash('Registration successful')
    return render_template("signup.html", form = form)

@myapp_obj.route("/pomodoro-timer", methods=['GET', 'POSTS'])
@login_required
def pomodoro():
    return render_template("pomodoro_timer.html")
