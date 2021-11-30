#class Card(UserMixin, db.Model):
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
        return f'Id: {self.id} [{self.front}, {self.back}]'
