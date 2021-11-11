from flask import Flask, render_template, request
app = Flask(_name_)

@app. route ("/upload")
def show_upload_form():
    return render_template("upload.html"

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    else:
        