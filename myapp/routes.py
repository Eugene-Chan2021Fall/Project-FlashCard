from myapp import myapp_obj
from myapp.convert import MarkdownConverter
import os, markdown, pdfkit
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from myapp.forms import *

from flask import render_template, flash, redirect, url_for, request
from myapp import db
from myapp.models import *
from flask_login import current_user, login_user, logout_user, login_required

#Home
@myapp_obj.route("/")
def home():
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

#-------------------------------------------------------------------------------

#Stats
@myapp_obj.route("/mystats")
def stats():
    '''
    This is the home route endpoint.

    Returns
    -------
    Renders the home.html template.
    '''
    hours_tracked = HoursTracked.query.get(current_user.get_id())

    #Calculate milisec to hours
    time = hours_tracked.time
    time = round(time/1000)
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600

    #Golden stars
    golden_stars = ""
    num_of_stars = 0
    for n in range(hour):
        golden_stars +=" X "
        num_of_stars += 1

    return render_template("user/stats.html", hours_tracked = hours_tracked, golden_stars = golden_stars, num = num_of_stars)
#Login/Sign up
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
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

@myapp_obj.route("/logout")
def logout():
    '''
    This is the logout route endpoint.

    Returns
    -------
    Redirects back to the home directory.
    '''
    logout_user()
    return redirect("/")

@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signup():
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

#-------------------------------------------------------------------------------

#Pomodoro
@myapp_obj.route("/pomodoro-timer")
@login_required
def pomodoro():
    '''
    This is the pomodoro timer route.

    Returns
    -------
    Renders the pomodoro_timer.html template.
    '''
    return render_template("user/pomodoro_timer.html")

#-------------------------------------------------------------------------------
#Timer
@myapp_obj.route("/posts", methods=['POST'])
def posts():
    '''
    This is a route that handles POST request from the user menu study timer.

    Returns
    -------
    Study session time.
    '''
    jsonobj = request.get_json()
    milisec = int(jsonobj["time"])
    hour_tracker = HoursTracked.query.get(current_user.get_id())
    hour_tracker.time += milisec
    db.session.commit()

    return '200'


#-------------------------------------------------------------------------------
#Flashcards
@myapp_obj.route("/flashcard")
@login_required
def display():
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

#Main Flashcard route handling adding, removing and displaying
@myapp_obj.route("/flashcard/<option>/<name>-<id>", methods=['GET', 'POST'])
@login_required
def flashcard(option, name, id):
    '''
    This is the route that handles many of the flashcard set's features
    such as adding Cards, removing Cards, and renaming the set.

    Defined Routes
    --------------
    /flashcard/add/<name>-<id> : Takes flashcard set name and the primary key
    Adds Cards to flashcard set.

    /flashcard/delete/<name>-<id> : Takes flashcard set name and the primary key
    Delete Cards to flashcard set.

    /flashcard/display/<name>-<id> : Takes flashcard set name and the primary key
    Display Cards in flashcard set.

    /flashcard/rename/<name>-<id> : Takes flashcard set name and the primary key
    Rename flashcard set.

    Parameters
    ----------
    GET : /flashcard/rename/<name>-<id>
    POST : Form data from each route.

    Returns
    -------
    Renders the flashcard_add_cards.html template.
    Renders the flashcard_delete_cards.html template.
    Renders the flashcard_display.html template.
    Renders the flashcard_edit_cards.html template. --Not implemented yet
    '''
    #Adding Card
    if (str(option).lower() == "add"):
        add_form = CardForm()
        if add_form.validate_on_submit():
            card = Card(front = add_form.front.data, back = add_form.back.data, set_id = id)
            db.session.add(card)
            db.session.commit()
            flash(f'Card has been added')
        return render_template('/flashcard/flashcard_add_cards.html', form=add_form,
         name=name, id=id)
    #---------------------------------------------------------------------------
    #Deleting Cards
    elif (str(option).lower() == "delete"):
        list = Card.query.filter_by(set_id = id)
        delete_form = DeleteForm()
        delete_form.delete.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list]

        if delete_form.validate_on_submit():
            card = Card.query.get(delete_form.delete.data)
            if card is None:
                flash('empty')
            else:
                db.session.delete(card)
                db.session.commit()
                flash(f'{card} has been removed.')
                return redirect(f'/flashcard/delete/{name}-{id}')
        return render_template('/flashcard/flashcard_delete_cards.html',form=
        delete_form, name=name, id=id)
    #---------------------------------------------------------------------------
    #Displaying Cards
    elif (str(option).lower() == "display"):
        list = Card.query.filter_by(set_id = id)
        return render_template('/flashcard/flashcard_display.html', name=name, id=id, list = list)

    #---------------------------------------------------------------------------
    #Rename Cards
    elif (str(option).lower() == "edit"):
        list = Card.query.filter_by(set_id = id)
        edit_form = CardEditForm()
        edit_form.select.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list] #Refresh Choices
        if edit_form.validate_on_submit():
            card = Card.query.get(edit_form.select.data)
            if card is None:
                flash('empty')
            else:
                if len(edit_form.front.data) == 0 or len(edit_form.back.data) == 0:
                    flash('Empty front/back.')
                else:
                    card.front = edit_form.front.data
                    card.back = edit_form.back.data
                    db.session.commit()
                    flash('Renamed card.')
                    edit_form.select.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list] #Refresh Choices
                    redirect(f'/flashcard/edit/{name}-{id}')
        return render_template('/flashcard/flashcard_edit_cards.html', name=name, id=id, form=edit_form)
    return str(option) + ' is a invalid route.'


#Creates flashcard set
@myapp_obj.route("/flashcard/create", methods=['GET', 'POST'])
@login_required
def create_sets():
    '''
    This is the route to create flashcard sets.

    Parameters
    ----------
    GET : /flashcard/create
    POST : new Flashcardset data
    Returns
    -------
    Renders the flashcard_create.html template.
    '''
    form = FlashcardForm()
    user = current_user.get_id()
    flash(f'Debug User Id: {user}')
    if form.validate_on_submit():
        set = Flashcardset(name = form.name.data, author_id = current_user.get_id())
        db.session.add(set)
        db.session.commit()
        return redirect(url_for('flashcard', option="display", name=set.name, id=set.id))
    return render_template("/flashcard/flashcard_create.html", form = form)

#Delete flashcard set
@myapp_obj.route("/flashcard/delete", methods=['GET', 'POST'])
@login_required
def delete_sets():
    '''
    This is the route to delete flashcard sets.

    Parameters
    ----------
    GET : /flashcard/delete
    POST : delete param
    Returns
    -------
    Renders the flashcard_delete.html template.
    Redirects back to /flashcard/delete
    '''
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form = DeleteForm()
    form.delete.choices = [(g.id, g.name) for g in list]
    if form.validate_on_submit():
        flashcard = Flashcardset.query.get(form.delete.data)
        if flashcard is None:
            flash('empty')
        else:
            db.session.delete(flashcard)
            db.session.commit()
            flash(f'{flashcard} has been removed.')
            return redirect('/flashcard/delete')
    return render_template('/flashcard/flashcard_delete.html', form=form)

#Upload Markdown file to flashcard
@myapp_obj.route("/flashcard/upload", methods=['GET', 'POST'])
@login_required
def upload():
    '''
    This is the route to upload a markdown file to make a flashcard set.

    Parameters
    ----------
    GET : /flashcard/upload
    POST : markdown file
    Returns
    -------
    Renders the flashcard_upload.html template.
    '''
    form = FileForm()
    mdc = MarkdownConverter

    if form.validate_on_submit():
        fr= form.file.data.read()
        list = fr.splitlines(False)
        mdc.convert(list)
    return render_template('/flashcard/flashcard_upload.html', form=form)

#Rename flashcard set
@myapp_obj.route("/flashcard/rename", methods=['GET', 'POST'])
@login_required
def rename_sets():
    '''
    This is the route to rename flashcard sets.

    Parameters
    ----------
    GET : /flashcard/rename
    POST : rename param, new name
    Returns
    -------
    Renders the flashcard/rename.html template.
    Redirects back to /flashcard/rename
    '''
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form = RenameForm()
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices

    if form.validate_on_submit():
        if len(form.name.data) == 0:
            flash('New name is empty.')
        else:
            flashcard = Flashcardset.query.get(form.select.data)
            if flashcard is None:
                flash('empty')
            else:
                flashcard.name = form.name.data
                db.session.commit()
                flash('Renaming sucessful')
                form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices
                return redirect('/flashcard/rename')
    return render_template("/flashcard/flashcard_rename.html", form=form)

#Share flashcards
@myapp_obj.route("/flashcard/share", methods=['GET', 'POST'])
@login_required
def flashcard_share():
    '''
    This is the route to share flashcard sets.

    Parameters
    ----------
    GET : /flashcard/rename
    POST : rename param, new name
    Returns
    -------
    Renders the flashcard/rename.html template.
    Redirects back to /flashcard/rename
    '''
    form = ShareForm()
    list = Flashcardset.query.filter_by(author_id = current_user.get_id())
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choices

    if form.validate_on_submit:
        checkName = User.query.filter_by(username = form.target.data)
        if checkName is None:
            flash('User not found.')
        elif form.select.data is None:
            flash('Pick a set')
        else:
            flashcard = Flashcardset.query.get(form.select.data)
            share = Flashcardshare(target = form.target.data, flashcard_id = form.select.data, flashcard_name = flashcard.name)
            db.session.add(share)
            db.session.commit()
            flash(f'Flashcard shared to {form.select.data}.')
            flash(f'Flashcard shared to {form.target.data}.')
    return render_template('/flashcard/flashcard_share.html', form=form)

#-------------------------------------------------------------------------------
#Todo-Tracker
@myapp_obj.route("/todo-tracker", methods=['GET', 'POST'])
@login_required
def todo_tracker():
    '''
    This is the route to display/add to the todo-tracker.

    Parameters
    ----------
    GET : /todo-tracker
    POST : tasks
    Returns
    -------
    Renders the todo-tracker.html template.
    '''
    add_form = TaskForm()
    list = Task.query.filter_by(author_id = current_user.get_id())
    if add_form.validate_on_submit():
        task = Task(task = add_form.task.data, author_id = current_user.get_id())
        db.session.add(task)
        db.session.commit()
        flash('Task added.')

    return render_template("/user/todo-tracker.html", add_form=add_form, list=list)

#Task remover
@myapp_obj.route("/todo-tracker/delete", methods=['GET', 'POST'])
@login_required
def todo_tracker_delete():
    '''
    This is the route to remove task from the todo-tracker.

    Parameters
    ----------
    GET : /todo-tracker/delete
    POST : delete param
    Returns
    -------
    Renders the todo-tracker_delete.html template.
    Redirects back to /todo-tracker/delete
    '''
    form = DeleteForm()
    list = Task.query.filter_by(author_id = current_user.get_id())
    form.delete.choices = [(g.id, g.task) for g in list]
    if form.validate_on_submit():
        task = Task.query.get(form.delete.data)
        db.session.delete(task)
        db.session.commit()
        flash(f'{task} removed.')
        return redirect('/todo-tracker/delete')

    return render_template("/user/todo-tracker_delete.html", form=form)

#Rename tasks
@myapp_obj.route("/todo-tracker/rename", methods=['GET', 'POST'])
@login_required
def rename_tasks():
    '''
    This is the route to rename tasks.

    Parameters
    ----------
    GET : /todo-tracker/rename
    POST : rename param, new name
    Returns
    -------
    Renders the todo-tracker/rename.html template.
    Redirects back to /todo-tracker/rename
    '''
    list = Task.query.filter_by(author_id = current_user.get_id())
    form = RenameForm()
    form.select.choices = [(g.id, g.task) for g in list] #Refresh Choices

    if form.validate_on_submit():
        if len(form.name.data) == 0:
            flash('New name is empty.')
        else:
            task = Task.query.get(form.select.data)
            if flashcard is None:
                flash('empty')
            else:
                task.task = form.name.data
                db.session.commit()
                flash('Renaming sucessful')
                form.select.choices = [(g.id, g.task) for g in list] #Refresh Choices
                return redirect('/todo-tracker/rename')
    return render_template("/user/todo-tracker_rename.html", form=form)


#-------------------------------------------------------------------------------
# Notes
@myapp_obj.route("/notes")
@login_required
def notes_portal():
    '''
    This is the route to display User's markdown notes.

    Returns
    -------
    Renders the notes_portal.html template.
    '''

    return render_template('notes/notes_portal.html')

# Notes Render
@myapp_obj.route("/notes/render", methods=['GET', 'POST'])
@login_required
def notes_render():
    '''
    This is the route to render User's markdown notes.

    GET : /notes/render
    POST : File data

    Returns
    -------
    Renders the notes_render.html template.
    '''
    html = ""
    form = FileForm()
    if form.validate_on_submit():
        text = form.file.data.read()
        newtext = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        html = newtext[4:-3].split('\\n')
    return render_template('notes/notes_render.html', form=form, html = html)

# Notes Markdown to Pdf
@myapp_obj.route("/notes/mark-to-pdf", methods=['GET', 'POST'])
@login_required
def notes_renderer():
    '''
    This is the route to take Markdown files and convert them to PDF.

    GET : /notes/mark-to-pdf
    POST : File data

    Returns
    -------
    Renders the notes_marktopdf.html template.
    '''

    form = FileForm()
    if form.validate_on_submit():
        text = form.file.data.read()
        text = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        pdfkit.from_string(text, 'note.pdf')
    return render_template('notes/notes_marktopdf.html', form=form)

#Make mindmap and save it to png file
@myapp_obj.route("/mindmap")
@login_required
def mindmap_pdf():
    '''
    This is the route to make mindmap.

    Returns
    -------
    Renders the mindmap.html template.
    '''
    g = nx.Graph()
    # flashcards = Flashcardset.query.filter_by(author_id = current_user.get_id()).get(1)
    # g.add_nodes_from(flashcards)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 5)

    nx.draw(g, with_labels = True)
    plt.savefig("plot.png")

    return render_template("mindmap.html")
