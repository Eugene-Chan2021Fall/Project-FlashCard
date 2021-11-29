from flask import Flask, render_template
import markdown
import os

filemd = os.path.join(app_obj.root_path,'md')
context_routes = []

##------------------------------------
#Render Markdown notes uing file.md
@app_obj.route("/rendMark")
@login_required
def rendMark():
    if os.path.isfile(filemd):
        with open(filemd) as mdfile:
              MDContent = markdown.markdown(mdfile.read(),
                              extensions=['fenced_code','codehilite'])
              else:
                         MDContent = None
              return render_template('rendMark.html', MDContent=MDContent, Routes=context_routes)
