from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1><u><i>Hello World</i></u></h1></body></body></hmtl>'
