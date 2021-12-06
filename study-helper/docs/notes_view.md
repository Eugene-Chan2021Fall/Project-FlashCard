#def notes_view():
    '''
    This is the route to render other User's note shared to you.

    GET : /notes/view
    POST : Note

    Returns
    -------
    Renders the notes_render.html template.
    '''
    html = ""
    user = User.query.get(current_user.get_id())
    list = Noteshare.query.filter_by(target = user.username)
    form = RenderForm()
    form.select.choices = [(g.note_id, g.note_name) for g in list] #Refresh Choice

    if form.validate_on_submit():
        note = Note.query.get(form.select.data)
        text = note.note
        newtext = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        html = newtext[4:-3].split('\\n')
    return render_template('notes/notes_render.html', form=form, html=html)
