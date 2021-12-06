#def notes_render():
    '''
    This is the route to render User's markdown notes.

    GET : /notes/render
    POST : File data

    Returns
    -------
    Renders the notes_render.html template.
    '''
    html = ""
    list = Note.query.filter_by(author_id = current_user.get_id())
    form = RenderForm()
    form.select.choices = [(g.id, g.name) for g in list] #Refresh Choice

    if form.validate_on_submit():
        note = Note.query.get(form.select.data)
        text = note.note
        newtext = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        html = newtext[4:-3].split('\\n')
    return render_template('notes/notes_render.html', form=form, html = html)
