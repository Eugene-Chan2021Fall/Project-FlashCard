from myapp import myapp_obj, pdf
from myapp.forms import LoginForm, SignupForm, FlashcardForm, FlashcardAddForm
from flask import render_template, flash, redirect, url_for

from myapp import db
from myapp.models import User, Flashcardset
from flask_login import current_user, login_user, logout_user, login_required

from myapp.pomodoro import PomodoroTimer

#Home
@myapp_obj.route("/")
def home():
    if current_user.is_authenticated:
        name = User.query.get(current_user.get_id()).username
        return render_template("user/user_home.html", name = name)
    return render_template("home.html")

#-------------------------------------------------------------------------------

#Login/Sign up
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect("login_templates/login")
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template("login_templates/login.html", form = form)

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
    return render_template("login_templates/signup.html", form = form)

#-------------------------------------------------------------------------------

#Pomodoro
@myapp_obj.route("/pomodoro-timer", methods=['GET', 'POST'])
@login_required
def pomodoro():
    return render_template("user/pomodoro_timer.html")


#-------------------------------------------------------------------------------
#Flashcards
@myapp_obj.route("/flashcard", methods=['GET', 'POST'])
@login_required
def display():
    flashcards = Flashcardset.query.filter_by(author_id = current_user.get_id())
    return render_template("/flashcard/flashcard_portal.html",
    flashcards = flashcards)

#Main Flashcard route handling adding, removing and displaying -- ignore for now
@myapp_obj.route("/flashcard/<option>/<name>", methods=['GET', 'POST'])
@login_required
def flashcard(option, name):
    if (str(option) == "add"):
        form = FlashcardAddForm()
        return render_template('/flashcard/flashcard_add_cards.html', form=form,
         name=name)
    elif (str(option) == "delete"):
        return "deleting flashcards"
    elif (str(option) == "display"):
        return render_template('/flashcard/flashcard_display.html', name=name)

    return str(option) + ' is a invalid route.'

#Creates flashcard set
@myapp_obj.route("/flashcard/create", methods=['GET', 'POST'])
@login_required
def create():
    form = FlashcardForm()
    user = current_user.get_id()
    flash(f'Debug User Id: {user}')
    if form.validate_on_submit():
        set = Flashcardset(name = form.name.data, author_id = current_user.get_id())
        flash(f'{set.name}')
        db.session.add(set)
        db.session.commit()
        return redirect(url_for('display', name = set.name))
    return render_template("/flashcard/flashcard_create.html", form = form)

#Edit flashcard set --ignore for now
@myapp_obj.route("/flashcard/edit", methods=['GET', 'POST'])
@login_required
def edit_sets():
    '''
    form = FlashcardAddForm()
    if form.validate_on_submit():
        return 'Works'
'''
    return render_template('/flashcard/flashcard_edit_sets.html', name=name)
