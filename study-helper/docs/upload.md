#def upload():
    '''
    This is the route to upload a markdown file to make a flashcard set.

    Parameters
    ----------
    GET : /flashcard/upload
    POST : markdown file
    Returns
    -------
    Renders the flashcard_upload.html template.
    '''
    form = FileForm()
    mdc = MarkdownConverter

    if form.validate_on_submit():
        fr= form.file.data.read()
        list = fr.splitlines(False)
        mdc.convert(list)
    return render_template('/flashcard/flashcard_upload.html', form=form)
