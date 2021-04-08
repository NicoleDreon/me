"""Server for me app."""

from flask import (Flask, render_template, request)

from model import connect_to_db

app = Flask(__name__)


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/login')
def login():
    """Log in."""

    user = request.form.get('user_name')
    print('hi')
    return user


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
