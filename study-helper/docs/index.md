# StudyHelper

StudyHelper is a webpage app that provides students with tools to get better
grades!

###Features
- Login/Signup Feature!
+ Pomodoro timer
+ Rename Files using Regular Expression
+ Track Hours Worked
+ Visualized Hours Worked
+ Input Markdown Files to Flashcards
+ Markdown to PDF Converter
+ Todo-Tracker
+ Share Flashcards to other Accounts
+ Render Markdown Notes


###Install

Run these commands if these have not been installed on your system.
```
sudo apt install pip3
sudo apt install wtfforms
sudo apt install flask
pip install pdfkit
pip install markdown
```

After finishing installing all these python packages, run
```python
python3 run.py
```
(NOTE: run.py is in your file directory)

## Project layout

    ├── gantt.xlsx          ---Our Planning Chart
    ├── myapp
    │   ├── app.db           ---Database File
    │   ├── convert.py            ---Convert Markdown files to Flashcards
    │   ├── forms.py         --WTForms for webpage
    │   ├── helper.md          --Markdown File used for testing
    │   ├── __init__.py        ----Init Flask and SQLAlchemy
    │   ├── models.py            ----------Database Models
    │   ├── pdf.py                -----Convert Mind map to PDF
    │   ├── __pycache__
    │   │   ├── convert.cpython-39.pyc
    │   │   ├── forms.cpython-39.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── pdf.cpython-39.pyc
    │   │   └── routes.cpython-39.pyc
    │   ├── rendMardown.py        -----------Not Implemented
    │   ├── routes.py                --------Handles routing for the webpage
    │   ├── static            ----A place to store static files such as js and css
    │   │   ├── css
    │   │   │   └── pomodoro.css
    │   │   └── js
    │   │       ├── pomodoro.js
    │   │       └── timer.js
    │   └── templates             ----Jinja HTML render templates
    │       ├── base.html
    │       ├── flashcard             ---------Flashcard HTML templates
    │       │   ├── flashcard_add_cards.html
    │       │   ├── flashcard_create.html
    │       │   ├── flashcard_delete_cards.html
    │       │   ├── flashcard_delete.html
    │       │   ├── flashcard_display.html
    │       │   ├── flashcard_edit_cards.html
    │       │   ├── flashcard_portal.html
    │       │   ├── flashcard_rename.html
    │       │   ├── flashcard_share.html
    │       │   └── flashcard_upload.html
    │       ├── helper.html
    │       ├── home.html
    │       ├── login_templates        ---Login HTML templates
    │       │   ├── login.html
    │       │   └── signup.html
    │       ├── mindmap.html
    │       ├── notes           -------Notes HTML templates
    │       │   ├── notes_marktopdf.html
    │       │   ├── notes_portal.html
    │       │   └── notes_render.html
    │       ├── rendMark.html
    │       └── user   ---------------User HTML templates
    │           ├── pomodoro_timer.html
    │           ├── stats.html
    │           ├── todo-tracker_delete.html
    │           ├── todo-tracker.html
    │           ├── todo-tracker_rename.html
    │           ├── user_home.html
    │           └── user_menu.html
    ├── README.md
    └── run.py             ------------Runs Flask for webpage
