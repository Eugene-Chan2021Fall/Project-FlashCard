#class Note(UserMixin, db.Model):
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
    note = db.Column(db.String(1024), index=True)
    share_id = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Id: {self.id} |{self.note}|'
