from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for)'hello_admin'))
    else:
        return redirect(url_for('hell_guest', guest = name))
