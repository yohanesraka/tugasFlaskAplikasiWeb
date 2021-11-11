from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/result')
def result ():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('results.html', result = dict)
