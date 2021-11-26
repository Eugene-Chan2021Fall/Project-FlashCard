import pdfkit
from myapp import myapp_obj
from flask import request

@myapp_obj.route('/mindmap')
def submit():
    if request.method == 'Post':
        if request.form['submit_button'] == 'Make PDF':
            pdfkit.from_file('mindmap.html', 'out.pdf')

