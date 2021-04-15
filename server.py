"""Server for me app."""

from flask import (Flask, render_template, request, flash, redirect, url_for, session, jsonify)

from model import connect_to_db

import crud

app = Flask(__name__)
app.secret_key = 'key'


@app.route('/')
def homepage():
    """View homepage."""

    if 'user_id' in session:
        return redirect('/past_entries')
    else:
        return render_template('homepage.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Log in."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.check_login(email)

    if user and user.email == email and user.password == password:
        session['user_id'] = user.user_id
        return redirect('/profile')
  
    else:
        flash('Invalid login information, try again.')
        return redirect('/')

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    """Create new user."""

    user = crud.get_user(session.get('user_id'))

    if 'user_id' in session:
        return redirect('/past_entries')

    else:
        return render_template('sign_up.html')

# if user not in session send to /
# if user in session
# display info by query db
@app.route('/profile')
def profile():
    """Display user profile information."""

    user_id = session.get('user_id')
    user = crud.get_user(user_id)
    # dry code => user = crud.get_user(session.get('user_id'))
  
    if 'user_id' in session:
        return render_template('profile.html', 
                                fname=user.fname,
                                lname=user.lname, 
                                email=user.email,
                                phone=user.phone,
                                password=user.password,
                                dob=user.dob,
                                gender=user.gender)
        
    else:    
        return render_template('homepage.html')
    
@app.route('/past_entries')
def past_entries():
    """Display past journal entries for user."""

    user = crud.get_user(session.get('user_id'))
    
    if 'user_id' in session:
        # dict = {date: morning, evening}
        return render_template('past_entries.html',
                                morning_entries=user.morning_entries,
                                evening_entries=user.evening_entries)

    else:
        return render_template('homepage.html')


@app.route('/logout')
def logout():
    """Log out."""

    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
