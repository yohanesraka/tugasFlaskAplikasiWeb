from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello (name=None):
    return render_template('hello.html', name=name)
