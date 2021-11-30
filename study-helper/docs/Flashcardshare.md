#class Flashcardshare(UserMixin, db.Model):
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
            return f'Id: {flashcard.id} |{flashcard.name}|'
        else:
            return None
