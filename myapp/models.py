from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from myapp import login


class User(UserMixin, db.Model):
    '''
    A class that represents a User.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    username : string
    email : string
    password : string
    flashcard_set : class Flashcardset --> author_id (Foreign Key)
    tasks : class Task --> author_id (Foreign Key)
    notes : class Note --> author_id (Foreign Key)

    Returns
    -------
    None
    '''
    #User information primary id, username, email, password
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password  = db.Column(db.String(128))

    #Relationships
    flashcard_set = db.relationship('Flashcardset', backref='author', lazy=True)
    tasks = db.relationship('Task', backref='author', lazy=True)
    notes = db.relationship('Note', backref='author', lazy=True)
    study_time = db.relationship('HoursTracked', backref='author', lazy=True)

    def set_password(self, password):
        '''
        Takes strings and hashs it to set as a User's Password.

        Parameters
        ----------
        password : str
        A password in str format.
        Returns
        -------
        None
        '''
        self.password = generate_password_hash(password)

    def check_password(self, password):
        '''
        Takes string and verifies the User's password in the database.

        Parameters
        ----------
        password : str
        A password in str format.

        Returns
        -------
        boolean
        If the password matches it returns True else False.
        '''
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}> |Sets : {self.flashcard_set}| Tasks: {self.tasks}'

#-------------------------------------------------------------------------------
#Time

class HoursTracked(UserMixin, db.Model):
    '''
    A class that represents the time a User has spent studying.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)

    author_id : int (Foreign Key) --> flashcard_set (class User)
    Relationship with User class.

    time : int
    Total time studied.

    Returns
    -------
    None
    '''
    #Flashcard set model that takes cards and puts them into a set.
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        #Mathematical Representation of time from seconds
        time = round(self.time/1000)
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        mins = time // 60
        time %= 60
        secs = time
        return f'|Days: {day} Hours: {hour} Mins: {mins} Secs: {secs}|'



#-------------------------------------------------------------------------------
#Flashcards

class Flashcardset(UserMixin, db.Model):
    '''
    A class that represents a Flashcard Set.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    author_id : int (Foreign Key) --> flashcard_set (class User)
    share_id : int (Foreign Key) --> share (class Flashcardshare)
    name : str
    cards : class Card --> set_id (Foreign Key)

    Returns
    -------
    None
    '''
    #Flashcard set model that takes cards and puts them into a set.
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    share_id = db.Column(db.Integer)
    name = db.Column(db.String(64), unique=False, index=True)
    cards = db.relationship('Card', backref='set', lazy=True)

    def __repr__(self):
        return f'|{self.name}|'


class Card(UserMixin, db.Model):
    '''
    A class that represents a Card.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    front : str
    back : str
    set_id : int (Foreign Key) --> cards (class Flashcardset)

    Returns
    -------
    None
    '''
    #Card Model that holds the front side and back side of a card and passes into Flashcard
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(256), index=True)
    back = db.Column(db.String(256), index=True)
    set_id = db.Column(db.Integer, db.ForeignKey('flashcardset.id'))

    def __repr__(self):
        return f'[{self.front}, {self.back}]'

class Flashcardshare(UserMixin, db.Model):
    '''
    A class that holds permissions of who can view notes.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    flashcard_id : int
    A flashcard primary_key.
    flashcard_name : str
    A flashcard name.
    target : int
    Another user's primary key.

    Returns
    -------
    None
    '''
    id = db.Column(db.Integer, primary_key=True)
    flashcard_id = db.Column(db.Integer)
    flashcard_name = db.Column(db.String)
    target = db.Column(db.Integer)

    def __repr__(self):
        flashcard = Flashcardset.query.get(self.flashcard_id)
        if flashcard is not None:
            return f'|{flashcard.name}|'
        else:
            return None


#-------------------------------------------------------------------------------
#Todo-tracker
class Task(UserMixin, db.Model):
    '''
    A class that represents a Task.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    task : str
    author_id : int (Foreign Key) --> notes (class User)

    Returns
    -------
    None
    '''
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'|{self.task}|'

#-------------------------------------------------------------------------------
#Notes
class Note(UserMixin, db.Model):
    '''
    A class that represents notes.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    note : str
    share_id : int class Note --> author_id (Foreign Key)
    author_id : int (Foreign Key) --> notes (class User)

    Returns
    -------
    None
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    note = db.Column(db.String(1024), index=True)
    share_id = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'|{self.name}|'

class Noteshare(UserMixin, db.Model):
    '''
    A class that holds permissions of who can view notes.

    Parameters
    ----------
    UserMixin : login tracker
    db.Model : db
    SQLalchemy database model.

    Model
    -----
    id : int (Primary Key)
    note_id : int
    A note's primary key.
    target : int
    Another user's primary key.

    Returns
    -------
    None
    '''
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer)
    note_name = db.Column(db.String)
    target = db.Column(db.Integer)

    def __repr__(self):
        return f'|{self.note_name}|'

@login.user_loader
def load_user(id):
    '''Login Manager function to loads users'''
    return User.query.get(int(id))
