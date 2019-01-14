#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return("That's Right :)")


if __name__ == "__main__":
    app.run(host="0", port=8585,  debug=1)
