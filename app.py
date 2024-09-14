from flask import Flask, redirect, render_template, url_for, request

from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')


if __name__ == '__main__':
    # Create the database tables

    app.run(port=3000,  debug=True)
