#class HoursTracked(UserMixin, db.Model):
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
        return f'ID: {self.id} |Days: {day} Hours: {hour} Mins: {mins} Secs: {secs}'
