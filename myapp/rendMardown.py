from flask import Flask, render_template
import markdown
import os

'''
Not Implemented yet

@app_obj.route("/")
def rendMark():
    if os.path.isfile(indexmd):
        with open(indexmd) as mdfile:
              MDContent = markdown.markdown(mdfile.read(),
                              extensions=['fenced_code','codehilite'])
              else:
                         MDContent = None
              return render_template('index.html, MDContent=MDContent, Routes=context_routes')
'''
