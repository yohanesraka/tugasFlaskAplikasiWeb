import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="databaseblogflask"
    )

    return mydb

def get_post(post_id):
    mydb = get_db_connection()
    cursor = mydb.cursor()
    cursor.execute(
        'SELECT * FROM posts WHERE id = %s',
        (post_id,)
    )

    result = cursor.fetchone()
    post = {
        'id': result[0],
        'created': result[1],
        'title': result[2],
        'content': result[3]
    }
    mydb.close()

    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    mydb = get_db_connection()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM posts')
    result = cursor.fetchall()

    posts = []
    for entry in result:
        record = {
            'id': entry[0],
            'created': entry[1],
            'title': entry[2],
            'content': entry[3]
        }
        posts.append(record)

    mydb.close()
    
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            mydb = get_db_connection()
            cursor = mydb.cursor()

            cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s)',
                         (title, content))
            mydb.commit()
            mydb.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            mydb = get_db_connection()
            cursor = mydb.cursor()

            cursor.execute('UPDATE posts SET title = %s, content = %s'
                         ' WHERE id = %s',
                         (title, content, id))
            mydb.commit()
            mydb.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    mydb = get_db_connection()

    cursor = mydb.cursor()

    cursor.execute('DELETE FROM posts WHERE id = %s', (id,))
    mydb.commit()
    mydb.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
