#class User(UserMixin, db.Model):
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
