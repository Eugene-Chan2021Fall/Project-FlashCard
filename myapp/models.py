from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from myapp import login


class User(UserMixin, db.Model):
    #User Model that holds id, username, email, password.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password  = db.Column(db.String(128))

    #Relationships
    flashcard_set = db.relationship('Flashcardset', backref='author', lazy=True)
    tasks = db.relationship('Task', backref='author', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}> |Sets : {self.flashcard_set}| Tasks: {self.tasks}'

#-------------------------------------------------------------------------------
#Flashcards
'''
WIP Sharing Model
class FlashcardSupport(db.Model):
    #Table that takes user_id to see what users should have access to certain flashcards
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    set_id = db.(db.Integer, db.ForeignKey('flashcardset.id'))
'''

class Flashcardset(UserMixin, db.Model):
    #Flashcard set model that takes cards and puts them into a set.
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64), unique=False, index=True)
    cards = db.relationship('Card', backref='set', lazy=True)

    def __repr__(self):
        return f'Id: {self.id} |{self.name}|'


class Card(UserMixin, db.Model):
    #Card Model that holds the front side and back side of a card and passes into Flashcard
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(256), index=True)
    back = db.Column(db.String(256), index=True)
    set_id = db.Column(db.Integer, db.ForeignKey('flashcardset.id'))

    def __repr__(self):
        return f'|[{self.front}, {self.back}] Id: {self.id}|'

#-------------------------------------------------------------------------------
#Todo-tracker
class Task(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Id: {self.id} |{self.task}|'
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
