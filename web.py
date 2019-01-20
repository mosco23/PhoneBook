#!/usr/bin/python3
from phonebook import PhoneBook
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return(render_template('index.html'))
    elif request.method == 'POST':
        name, phoneNumber, email = request.form['name'], request.form['phoneNumber'], request.form['email']
        submit = PhoneBook(name, phoneNumber, email)
        submit.submit()
        return('Information was recorded successfully')


if __name__ == "__main__":
    app.run(host="0", port=8585,  debug=1)
