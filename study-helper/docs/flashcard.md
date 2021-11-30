#def flashcard(option, name, id):
    '''
    This is the route that handles many of the flashcard set's features
    such as adding Cards, removing Cards, and renaming the set.

    Defined Routes
    --------------
    /flashcard/add/<name>-<id> : Takes flashcard set name and the primary key
    Adds Cards to flashcard set.

    /flashcard/delete/<name>-<id> : Takes flashcard set name and the primary key
    Delete Cards to flashcard set.

    /flashcard/display/<name>-<id> : Takes flashcard set name and the primary key
    Display Cards in flashcard set.

    /flashcard/rename/<name>-<id> : Takes flashcard set name and the primary key
    Rename flashcard set.

    Parameters
    ----------
    GET : /flashcard/rename/<name>-<id>
    POST : Form data from each route.

    Returns
    -------
    Renders the flashcard_add_cards.html template.
    Renders the flashcard_delete_cards.html template.
    Renders the flashcard_display.html template.
    Renders the flashcard_edit_cards.html template. --Not implemented yet
    '''
    #Adding Card
    if (str(option).lower() == "add"):
        add_form = CardForm()
        if add_form.validate_on_submit():
            card = Card(front = add_form.front.data, back = add_form.back.data, set_id = id)
            db.session.add(card)
            db.session.commit()
            flash(f'Card has been added')
        return render_template('/flashcard/flashcard_add_cards.html', form=add_form,
         name=name, id=id)
    #---------------------------------------------------------------------------
    #Deleting Cards
    elif (str(option).lower() == "delete"):
        list = Card.query.filter_by(set_id = id)
        delete_form = DeleteForm()
        delete_form.delete.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list]

        if delete_form.validate_on_submit():
            card = Card.query.get(delete_form.delete.data)
            if card is None:
                flash('empty')
            else:
                db.session.delete(card)
                db.session.commit()
                flash(f'{card} has been removed.')
                return redirect(f'/flashcard/delete/{name}-{id}')
        return render_template('/flashcard/flashcard_delete_cards.html',form=
        delete_form, name=name, id=id)
    #---------------------------------------------------------------------------
    #Displaying Cards
    elif (str(option).lower() == "display"):
        list = Card.query.filter_by(set_id = id)
        return render_template('/flashcard/flashcard_display.html', name=name, id=id, list = list)

    #---------------------------------------------------------------------------
    #Rename Cards
    elif (str(option).lower() == "edit"):
        list = Card.query.filter_by(set_id = id)
        edit_form = CardEditForm()
        edit_form.select.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list] #Refresh Choices
        if edit_form.validate_on_submit():
            card = Card.query.get(edit_form.select.data)
            if card is None:
                flash('empty')
            else:
                if len(edit_form.front.data) == 0 or len(edit_form.back.data) == 0:
                    flash('Empty front/back.')
                else:
                    card.front = edit_form.front.data
                    card.back = edit_form.back.data
                    db.session.commit()
                    flash('Renamed card.')
                    edit_form.select.choices = [(g.id, f'[{g.front}, {g.back}]') for g in list] #Refresh Choices
                    redirect(f'/flashcard/edit/{name}-{id}')
        return render_template('/flashcard/flashcard_edit_cards.html', name=name, id=id, form=edit_form)
    return str(option) + ' is a invalid route.'
