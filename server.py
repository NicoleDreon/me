"""Server for me app."""

from flask import (Flask, render_template, request, flash, redirect, url_for, session, jsonify)

from model import connect_to_db
from datetime import datetime

import crud
import zen_quotes
import helper_functions

app = Flask(__name__)
app.secret_key = 'key'


@app.route('/')
def homepage():
    """View homepage."""

    quote = zen_quotes.get_quote()
    print(quote)
    if 'user_id' in session:
        return redirect('/past_entries')
    else:
        return render_template('homepage.html', quote=quote)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Log in."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.check_login(email)

    if user and user.email == email and user.password == password:
        session['user_id'] = user.user_id
        return redirect('/past_entries')
  
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


@app.route('/profile')
def profile():
    """Display user profile information."""
  
    if 'user_id' in session:
        user_id = session.get('user_id')
        user = crud.get_user(user_id)
        fname = user.fname
        # dry code => user = crud.get_user(session.get('user_id'))
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

@app.route('/profile', methods=['POST'])
def get_new_user_info():
    """Get new user info."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    # ????????????????????????
    dob = datetime.today()
    gender = request.form.get('gender')
    print(password)
    # check_login with email that was given
    # if it returns user redirect to login - flash message user exists
    # if returns none(else) implement the rest of function
    new_user = crud.add_user(fname, lname, email, phone, dob, gender, password)

    session['user_id'] = new_user.user_id

    return render_template('profile.html', fname=fname, lname=lname, email=email, phone=phone, password=password, dob=dob, gender=gender)
    
@app.route('/past_entries', methods=['GET', 'POST'])
def past_entries():
    """Display past journal entries for user."""

    if 'user_id' in session:

        quote = zen_quotes.get_quote()
        user = crud.get_user(session.get('user_id'))
        user_id = user.user_id
        entries = crud.get_entries(user_id)
        print(entries)
        print(quote)
        
        return render_template('past_entries.html', entries=entries, quote=quote)

    else:
        return render_template('homepage.html')


@app.route('/handle_new_am_entry', methods=['POST'])
def add_new_am_entry():
    """Add new morning entry to db."""

    date = request.form.get('date')
    hrs_sleep = helper_functions.cast_float(request.form.get('hrs-sleep'))
    qual_sleep = helper_functions.cast_int(request.form.get('qual-sleep'))
    snooze = helper_functions.cast_int(request.form.get('snooze'))
    goal = request.form.get('goal')
    journal_entry = request.form.get('journal-entry')
    entries = request.form.getlist('gratitude')
    reasons = request.form.getlist('gratitude-reason')

    if crud.get_am_entry_by_date(date):
        flash('Morning entry for this day alreay exists')
        return redirect('/new_am_entry')

    else:
        new_am_entry = crud.add_am_entry(session['user_id'], date, hrs_sleep, qual_sleep, snooze, goal, journal_entry)
        new_gratitude = crud.add_am_entries_gratitudes(new_am_entry.am_entry_id, entries, reasons)

        return redirect('/past_entries')


@app.route('/handle_new_pm_entry', methods=['POST'])
def add_new_pm_entry():
    """Add new evening entry to db."""

    date = request.form.get('date')
    activity_level = request.form.get('activity-level')
    qual_day = request.form.get('qual-day')
    goal_completed = bool(helper_functions.cast_int((request.form.get('goal-completed'))))
    journal_entry = request.form.get('journal-entry')

    if crud.get_pm_entry_by_date(date):
        flash('Evening entry for this day alreay exists')
        return redirect('/new_pm_entry')

    else:
        new_pm_entry = crud.add_pm_entry(session['user_id'], date, activity_level, qual_day, goal_completed, journal_entry)

        return redirect('/past_entries')


@app.route('/new_am_entry')
def new_am_entry():
    """Create a new morning entry."""
    
    if 'user_id' in session:
        user = crud.get_user(session.get('user_id'))
        user_id = user.user_id
    
        return render_template('new_am_entry.html')
   
    else:
        return redirect('/')   

@app.route('/new_pm_entry')
def new_pm_route():
    """Create a new evening entry."""

    if 'user_id' in session:
        user = crud.get_user(session.get('user_id'))
        user_id = user.user_id

        return render_template('new_pm_entry.html')

    else:
        return redirect('/')

@app.route('/add_missing_am_entry')
def add_missing_am_entry():
    """Add a missing am entry."""

    date = request.args.get('date')
    date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    date_formated = date_time.strftime('%Y-%m-%d')
    print(date_formated)

    return render_template('add_missing_am_entry.html', date=date_formated)

@app.route('/add_missing_pm_entry')
def add_missing_pm_entry():
    """Add a missing pm entry."""

    date = request.args.get('date')
    date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    date_formated = date_time.strftime('%Y-%m-%d') 

    return render_template('add_missing_pm_entry.html', date=date_formated)

@app.route('/chart.json')
def chart():
    """Send data to front end."""

    am_entries = crud.get_am_entry_by_date_range()
    pm_entries = crud.get_pm_entry_by_date_range()

    data_dict = {}

    for entry in am_entries:
        data_dict[entry.date.strftime('%Y-%m-%d')] = {'hrs_sleep': str(entry.hrs_sleep), 'qual_sleep': entry.qual_sleep, 'snooze': entry.snooze}
    
        print(entry.date.strftime('%Y-%m-%d'))

    for entry in pm_entries:
        if entry.date.strftime('%Y-%m-%d') in data_dict:
            data_dict[entry.date.strftime('%Y-%m-%d')]['qual_day'] = entry.qual_day
            data_dict[entry.date.strftime('%Y-%m-%d')]['activity_level'] = entry.activity_level
            data_dict[entry.date.strftime('%Y-%m-%d')]['goal_completed'] = entry.goal_completed
        else:
            data_dict[entry.date.strftime('%Y-%m-%d')] = {'qual_day': entry.qual_day, 'activity_level': entry.activity_level, 'goal_completed': entry.goal_completed}

    print(data_dict)
    
    return jsonify(data_dict)
    

@app.route('/display_chart')
def display_chart():
    """Display chart of user data."""

    return render_template('chart.html')


@app.route('/logout')
def logout():
    """Log out."""

    session.pop('user_id', None)
    return redirect('/')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
