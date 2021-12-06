#class Noteshare(UserMixin, db.Model):
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
