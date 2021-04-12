"""Server for me app."""

from flask import (Flask, render_template, request, flash, redirect, url_for, session, jsonify)

from model import connect_to_db

import crud

app = Flask(__name__)
app.secret_key = 'key'


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def login():
    """Log in."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.check_login(email)

    # print(user)
    # print(user.user_id)

    if user and user.email == email and user.password == password:
        session['user_id'] = user.user_id
        session['fname'] = user.fname
        # user_id = session.get('user_id') - will return none if nothing
        # session['user'] = user.to_dict()
        print(user)
        print(user.fname)
        print(user.user_id)
    else:
        flash('Invalid login information, try again.')
        return redirect(url_for('homepage'))
    return render_template('profile.html')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
