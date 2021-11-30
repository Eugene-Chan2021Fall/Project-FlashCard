from flask import render_template, flash, redirect, url_for
from myapp import db
from myapp.models import User, Flashcardset, Card
from flask_login import current_user, login_user, logout_user, login_required

class MarkdownConverter:
    '''
    A class that converts Markdown Files and formarts it into flashcards.

    Methods
    -------
    read():
    Reads a markdown file.

    convert(list):
    Takes a list and converts it into flashcard format.
    '''

    def read(read, file):
        '''
        Reads markdown file.

        Parameters
        ----------
        file : str
        a file directory

        read : str
        param to pass into the read function

        Return
        ------
        list : list
        Takes the information being read and splits it into a list to be
        handled by the convert method.
        '''
        f = open(file, 'r')
        text = f.read()
        f.close()

        list = text.splitlines()
        return list

    def convert(list):
        '''
        Converts markdown file and adds it to the database.

        Parameters
        ----------
        list : list
        a list full of strings that represent the flashcard set

        read : str
        param to pass into the read function

        Returns
        -------
        None

        Example
        -------
        Files must be provided in this format.
        Each card must have a front and back or else the program will not accept
        the markdown file.

        #Title of flashcard set
        front
        back

        Ex:1
        #Homework Flashcard set
        Apple
        A red fruit used for apple pie.
        Kiwi
        Green fruit that is green.

        '''
        set = None   #flashcard set_id
        if len(list) == 0:  #checks for empty list
            flash('empty')
            return None
        else:
            if list[0][0] != "#" and list[0][1] == ' ':   #checks the first character of the first element
                flash('invalid name')
                return None
            else:
                num = 0
                if (len(list) - 1) % 2 != 0:    #checks if the md file follows the format
                    flash('invalid format')
                    return None
                else:                           #format title
                    flashcard = Flashcardset(name = list[0][2:], author_id = current_user.get_id())
                    db.session.add(flashcard)
                    db.session.commit()
                    set = flashcard.id
                for n in range(1, len(list), 2):  #adds the flashcards to the db
                        card = Card(front = list[n], back = list[n+1], set_id = set)
                        db.session.add(card)
                        db.session.commit()
        flash('File Uploaded')
