from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello-js.html")
