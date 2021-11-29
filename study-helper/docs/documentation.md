#convert.py
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField, SelectField, SelectMultipleField
    from wtforms.validators import DataRequired
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
[class Flashcardset:](/Flashcardset)<br>
[class Card:](/Card)<br>
[class Flashcardshare:](/Flashcardshare)<br>
[class Task:](/Task)<br>
[class Note:](/Note)<br>
[class FileForm:](/FileForm)<br>
[class RenameForm:](/RenameForm)<br>
[class CardEditForm:](/CardEditForm)<br>
[class ShareForm:](/ShareForm)<br>
