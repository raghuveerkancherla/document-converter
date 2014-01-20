import sqlite3
from flask import Flask, render_template, g, request, redirect
from contextlib import closing
from werkzeug import secure_filename
import os

#configuration
DATABASE = 'app.db'
USERNAME = 'aplopio'
PASSWORD = 'recruiterbox'
SECRET_KEY = 'development key'
DEBUG = True
UPLOAD_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = ['pdf', 'txt', 'html']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods = ['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            g.db.execute('insert into file_table (initial_file_path) values ("%s")'%(file_path))
            return redirect('/list')
        else:
            return "Only pdf, html and txt are supported."
    return render_template('root.html')

@app.route('/list/')
def list():
    cur = g.db.execute('select initial_file_path from file_table order by id desc')
    for c in cur.fetchall():
        print c
    return render_template('list.html')

if __name__ == '__main__':
    app.run()
