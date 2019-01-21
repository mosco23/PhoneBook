#!/usr/bin/python3
from phonebook import PhoneBook
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return(render_template('index.html'))
    elif request.method == 'POST':
        if 'submit_btn' in request.form:
            name, phoneNumber, email = request.form['name'], request.form['phoneNumber'], request.form['email']
            submit = PhoneBook(name, phoneNumber, email)
            submit.submit()
            return('Information was recorded successfully')
        elif 'search_btn' in request.form:
            global value
            value = request.form['search-engin']
            return(redirect('/search'))
        else:
            return()


@app.route('/search')
def search():
    c = len(value)
    f = open("static/.Phone_Lists.txt", "r")
    read = f.readlines()
    return(render_template('search-page.html', c=c, f=f, read=read, value=value))


if __name__ == "__main__":
    app.run(host="0", port=8585,  debug=1)
