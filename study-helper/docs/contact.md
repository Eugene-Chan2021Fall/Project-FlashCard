#def contact():
    '''
    Route that exports mindmap as a pdf.

    Returns
    -------
    Renders mindmap.html
    '''
    if 'submit_button' in request.form:
        pdfkit.from_file('mindmap.html', 'out.pdf')
    return render_template('mindmap.html')
