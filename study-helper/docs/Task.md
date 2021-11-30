#class Task(UserMixin, db.Model):
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
        return f'Id: {self.id} |{self.task}|'
