from myapp import myapp_obj, pdf
from myapp.convert import MarkdownConverter
import os

from myapp.forms import LoginForm, SignupForm
from myapp.forms import FlashcardForm, CardAddForm, CardDeleteForm, FlashcardDeleteForm
from myapp.forms import TaskForm, TaskDeleteForm
from myapp.forms import FileForm
from werkzeug.utils import secure_filename #*

from flask import render_template, flash, redirect, url_for
from myapp import db
from myapp.models import User, Flashcardset, Card, Task
from flask_login import current_user, login_user, logout_user, login_required
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

#Main Flashcard route handling adding, removing and displaying
@myapp_obj.route("/flashcard/<option>/<name>-<id>", methods=['GET', 'POST'])
@login_required
def flashcard(option, name, id):
    #Adding Card
    if (str(option) == "add"):
        add_form = CardAddForm()
        if add_form.validate_on_submit():
            card = Card(front = add_form.front.data, back = add_form.back.data, set_id = id)
            db.session.add(card)
            db.session.commit()
            flash(f'Card has been added')
        return render_template('/flashcard/flashcard_add_cards.html', form=add_form,
         name=name, id=id)
    #Deleting Cards
    elif (str(option) == "delete"):
        list = Card.query.filter_by(set_id = id)
        delete_form = CardDeleteForm()
        if delete_form.validate_on_submit():
            card = Card.query.get(delete_form.delete.data)
            if card is not None and int(id) == int(card.set_id):
                db.session.delete(card)
                db.session.commit()
                flash(f'{card} has been removed.')
            else:
                flash(f'Invalid ID')
        return render_template('/flashcard/flashcard_delete_cards.html', list=list ,form=
        delete_form, name=name, id=id)
    #Displaying Cards
    elif (str(option) == "display"):
        list = Card.query.filter_by(set_id = id)
        return render_template('/flashcard/flashcard_display.html', name=name, id=id, list = list)

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
        db.session.add(set)
        db.session.commit()
        return redirect(url_for('flashcard', option="display", name=set.name, id=set.id))
    return render_template("/flashcard/flashcard_create.html", form = form)

#Edit flashcard set --ignore for now
@myapp_obj.route("/flashcard/delete", methods=['GET', 'POST'])
@login_required
def delete_sets():
    checkUser = current_user.get_id()
    flashcards = Flashcardset.query.filter_by(author_id = checkUser)
    delete_form = FlashcardDeleteForm()
    if delete_form.validate_on_submit():
        flashcard = Flashcardset.query.get(delete_form.delete.data)
        #Deleting Process --Needs to be replaced later
        if flashcard is not None and flashcard.author_id == int(checkUser):
            db.session.delete(flashcard)
            db.session.commit()
            flash(f'{flashcard} has been removed.')
        else:
            flash('Invalid ID.')
    return render_template('/flashcard/flashcard_delete.html', form=delete_form,
    flashcards=flashcards)

#Upload Markdown file to flashcard
@myapp_obj.route("/flashcard/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = FileForm()
    mdc = MarkdownConverter

    if form.validate_on_submit():
        f = secure_filename(form.file.data.filename)
        fr= form.file.data.read().strip()
        list = fr.splitlines(False)
        mdc.convert(list)
    return render_template('/flashcard/flashcard_upload.html', form=form)


#-------------------------------------------------------------------------------
#Todo-Tracker
@myapp_obj.route("/todo-tracker", methods=['GET', 'POST'])
@login_required
def todo_tracker():
    add_form = TaskForm()
    list = Task.query.filter_by(author_id = current_user.get_id())
    if add_form.validate_on_submit():
        task = Task(task = add_form.task.data, author_id = current_user.get_id())
        db.session.add(task)
        db.session.commit()
        flash('Task added.')

    return render_template("/user/todo-tracker.html", add_form=add_form, list=list)

@myapp_obj.route("/todo-tracker/delete", methods=['GET', 'POST'])
@login_required
def todo_tracker_delete():
    checkUser = current_user.get_id()
    delete_form = TaskDeleteForm()
    list = Task.query.filter_by(author_id = checkUser)
    if delete_form.validate_on_submit():
        task = Task.query.get(delete_form.delete.data)
        #Deleting Process --Needs to be replaced later
        if task is not None and task.author_id == int(checkUser):
            db.session.delete(task)
            db.session.commit()
            flash('Task deleted.')
        else:
            flash('Invalid ID.')
    return render_template("/user/todo-tracker_delete.html", delete_form=delete_form, list=list)
