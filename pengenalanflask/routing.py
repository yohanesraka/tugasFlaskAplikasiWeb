from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hi')
def hi():
    return 'Hi, Guys'
