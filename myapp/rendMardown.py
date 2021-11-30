from flask import Flask, render_template
import markdown
import os

filemd = os.path.join(app_obj.root_path,'md','file.md')
context_routes = []

##------------------------------------
#Render Markdown notes uing file.md
@app_obj.route("/rendMark")
@login_required
def rendMark():
    '''
    reads file.md file 
    Parameter
    -------
    file: file.md 
     a file in directory
    Return
    ------
    Markdown file

    '''
    if os.path.isfile(filemd):
        with open(filemd) as mdfile:
              MDContent = markdown.markdown(mdfile.read(),
                              extensions=['fenced_code','codehilite'])
              else:
                         MDContent = None
              return render_template('rendMark.html', MDContent=MDContent, Routes=context_routes)
