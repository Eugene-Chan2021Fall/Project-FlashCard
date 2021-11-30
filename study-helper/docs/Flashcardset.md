#class Flashcardset(UserMixin, db.Model):
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
        return f'Id: {self.id} |{self.name}|'
