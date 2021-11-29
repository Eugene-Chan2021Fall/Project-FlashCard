# Study Helper

For full documentation visit [mkdocs.org](https://www.mkdocs.org).




###Before you do anything
Run these commands in your terminal to download Python
modules

```bash
sudo apt install pip3
sudo apt install wtfforms
sudo apt install flask
```
and others too if encounter any issues while running program

After finishing installing all these python packages, run
```python
python3 run.py
```
(NOTE: run.py is in your file directory)

## Commands
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


## Project layout

    ├── gantt.xlsx
    ├── myapp
    │   ├── app.db
    │   ├── convert.py
    │   ├── forms.py
    │   ├── helper.md
    │   ├── __init__.py
    │   ├── models.py
    │   ├── pdf.py
    │   ├── __pycache__
    │   │   ├── convert.cpython-39.pyc
    │   │   ├── forms.cpython-39.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── pdf.cpython-39.pyc
    │   │   └── routes.cpython-39.pyc
    │   ├── rendMardown.py
    │   ├── routes.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── pomodoro.css
    │   │   └── js
    │   │       ├── pomodoro.js
    │   │       └── timer.js
    │   └── templates
    │       ├── base.html
    │       ├── flashcard
    │       │   ├── flashcard_add_cards.html
    │       │   ├── flashcard_create.html
    │       │   ├── flashcard_delete_cards.html
    │       │   ├── flashcard_delete.html
    │       │   ├── flashcard_display.html
    │       │   ├── flashcard_edit_sets.html
    │       │   ├── flashcard_portal.html
    │       │   └── flashcard_upload.html
    │       ├── helper.html
    │       ├── home.html
    │       ├── login_templates
    │       │   ├── login.html
    │       │   └── signup.html
    │       ├── mindmap.html
    │       ├── rendMark.html
    │       └── user
    │           ├── pomodoro_timer.html
    │           ├── todo-tracker_delete.html
    │           ├── todo-tracker.html
    │           ├── user_home.html
    │           └── user_menu.html
    ├── run.py
    └── study-helper
        ├── docs
        │   ├── about.md
        │   └── index.md
        └── mkdocs.yml
