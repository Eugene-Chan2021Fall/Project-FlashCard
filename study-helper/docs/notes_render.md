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
    form = FileForm()
    if form.validate_on_submit():
        text = form.file.data.read()
        newtext = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        html = newtext[4:-3].split('\\n')
    return render_template('notes/notes_render.html', form=form, html = html)
