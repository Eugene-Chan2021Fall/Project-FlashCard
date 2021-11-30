#convert.py
    from flask import render_template, flash, redirect, url_for
    from myapp import db
    from myapp.models import User, Flashcardset, Card
    from flask_login import current_user, login_user, logout_user, login_required
[class MarkdownConverter:](/MarkdownConverter)

#forms.py
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField, SelectField, SelectMultipleField
    from wtforms.validators import DataRequired

[class LoginForm:](/LoginForm)<br>
[class SignupForm:](/SignupForm)<br>
[class FlashcardForm:](/FlashcardForm)<br>
[class CardForm:](/CardForm)<br>
[class TaskForm:](/TaskForm)<br>
[class DeleteForm:](/DeleteForm)<br>
[class FileForm:](/FileForm)<br>
[class RenameForm:](/RenameForm)<br>
[class CardEditForm:](/CardEditForm)<br>
[class ShareForm:](/ShareForm)<br>

#models.py
    from myapp import db
    from datetime import datetime
    from werkzeug.security import generate_password_hash, check_password_hash

    from flask_login import UserMixin
    from myapp import login

[class User:](/User)<br>
[class HoursTracked:](/HoursTracked)<br>
[class Flashcardset:](/Flashcardset)<br>
[class Card:](/Card)<br>
[class Flashcardshare:](/Flashcardshare)<br>
[class Task:](/Task)<br>
[class Note:](/Note)<br>
[class Noteshare:](/Noteshare)<br>

#routes.py
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

[def home():](/home)<br>
[def stats():](/stats)<br>
[def login():](/login)<br>
[def logout():](/logout)<br>
[def signup():](/signup)<br>
[def pomodoro():](/pomodoro)<br>
[def posts():](/posts)<br>
[def display():](/display)<br>
[def flashcard(option, name, id):](/flashcard)<br>
[def create_sets():](/create_sets)<br>
[def delete_sets:](/delete_sets)<br>
[def upload():](/upload)<br>
[def rename_sets():](/rename_sets)<br>
[def flashcard_share():](/flashcard_share)<br>
[def todo_tracker():](/todo_tracker)<br>
[def todo_tracker_delete():](/todo_tracker_delete)<br>
[def rename_tasks():](/rename_tasks)<br>
[def notes_portal():](/notes_portal)<br>
[def notes_render():](/notes_render)<br>
[def notes_renderer:](/notes_renderer)<br>
[def mindmap_pdf():](/mindmap)<br>
