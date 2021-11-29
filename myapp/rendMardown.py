from flask import Flask, render_template
import markdown
import os

filemd = os.path.join(app_obj.root_path,'md')
context_routes = []

@app_obj.route("/")
def rendMark():
    if os.path.isfile(filemd):
        with open(filemd) as mdfile:
              MDContent = markdown.markdown(mdfile.read(),
                              extensions=['fenced_code','codehilite'])
              else:
                         MDContent = None
              return render_template('rendMark.html, MDContent=MDContent, Routes=context_routes')
