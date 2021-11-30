#def notes_renderer():
    '''
    This is the route to take Markdown files and convert them to PDF.

    GET : /notes/mark-to-pdf
    POST : File data

    Returns
    -------
    Renders the notes_marktopdf.html template.
    '''

    form = FileForm()
    if form.validate_on_submit():
        text = form.file.data.read()
        text = str(text).replace("<p>b'", '').replace("'</p>",'')    # Reads Markdown and Displays as string
        pdfkit.from_string(text, 'note.pdf')
    return render_template('notes/notes_marktopdf.html', form=form)
