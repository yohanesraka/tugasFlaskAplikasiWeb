from flask import Flask, render_template, request
app = Flask(_name_)

@app. route ("/")
def index():
    return render_template("login-form.html", error=None)

def valid_login(uname, pwd):
    if uname == 'indrahid' and pwd =='dts2021':
        return True
    else :
        return False

def log_the _user_in(uname) :
return "SELAMAT!<br/>"+uname+" telah berhasil login."

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login (request. form['username'],
                        request. form['password']) :
        return log the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login-form.html', error=error)
