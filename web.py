#!/usr/bin/python3
import sqlite3
from phonebook import PhoneBook
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    db = sqlite3.connect('database.db')
    c = db.cursor()
    c.execute("SELECT * FROM Post")
    data = c.fetchall()
    db.close()
    if request.method == 'GET':
        return(render_template('index.html', data=data))
    elif request.method == 'POST':
        if 'submit_btn' in request.form:
            name, phoneNumber, email = request.form['name'], request.form['phoneNumber'], request.form['email']
            submit = PhoneBook(name, phoneNumber, email)
            submit.submit()
            return('Information was recorded successfully')
        elif 'search_btn' in request.form:
            db = sqlite3.connect('database.db')
            c = db.cursor()
            c.execute("SELECT * FROM Post WHERE Names='{}'".format(request.form['search-engin']))
            global value
            value = c.fetchall()
            db.close()
            return(redirect('/search'))
        else:
            return()


@app.route('/search')
def search():
    return(render_template('search-page.html', data=value))


if __name__ == "__main__":
    app.run(host="0", port=8585,  debug=1)
