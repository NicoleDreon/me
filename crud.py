"""CRUD operations."""

from model import db, User, Morning_Entry, Gratitude, Evening_Entry, Emotion_Entry, Emotion, connect_to_db

import datetime

def check_login(email):
  """Check if user exists in db."""
    
  return User.query.filter_by(email=email).first()


def get_user(user_id):
  """Return user by id."""

  return User.query.filter_by(user_id=user_id).first()


def add_user(fname, lname, email, phone, dob, gender, password):
  """Add new user to db."""

  new_user = User(fname=fname, lname=lname, email=email, phone=phone, password=password, dob=dob, gender=gender)

  db.session.add(new_user)
  db.session.commit()

  return new_user


def get_entries(user_id):
  """Create relationship between morning_entries and evening_entries tables for a speific user_id."""

  q = db.session.query(Morning_Entry, Evening_Entry)
  q = q.outerjoin(Evening_Entry, db.and_(Morning_Entry.date==Evening_Entry.date, Morning_Entry.user_id==Evening_Entry.user_id), full=True)
  q = q.filter(db.or_(Morning_Entry.user_id==user_id, Evening_Entry.user_id==user_id))
  q = q.order_by(Morning_Entry.date.desc(), Evening_Entry.date.desc())
  entries = q.all()

  return entries


def add_am_entry(user_id, date, hrs_sleep, qual_sleep, snooze, goal, journal_entry):
  """Add new morning journal entry."""

  new_am_entry = Morning_Entry(user_id=user_id, date=date, hrs_sleep=hrs_sleep, qual_sleep=qual_sleep, snooze=snooze, goal=goal, journal_entry=journal_entry)

  db.session.add(new_am_entry)
  db.session.commit()

  return new_am_entry


def add_gratitude_entry(am_entry_id, entry, reason):
  """Add new gratitude entry."""

  new_gratitude_entry = Gratitude(am_entry_id=am_entry_id, entry=entry, reason=reason)

  db.session.add(new_gratitude_entry)
  db.session.commit()

  return new_gratitude_entry

def add_am_entries_gratitudes(am_entry_id, entries, reasons):
  """Add gratitudes to morning entry."""
    
  if len(entries) != len(reasons):
    return 'not matched'
  
  for i in range(len(entries)):
    entry = entries[i]
    reason = reasons[i]

    add_gratitude_entry(am_entry_id, entry, reason)

  return 'success'


def add_pm_entry(user_id, date, activity_level, qual_day, goal_completed, journal_entry):
  """Add new evening journal entry."""

  new_pm_entry = Evening_Entry(user_id=user_id, date=date, activity_level=activity_level, qual_day=qual_day, goal_completed=goal_completed, journal_entry=journal_entry)

  db.session.add(new_pm_entry)
  db.session.commit()

  return new_pm_entry


def get_am_entry_by_date(date):
  """Return morning entry by date."""

  return Morning_Entry.query.filter_by(date=date).first()


def get_pm_entry_by_date(date):
  """Return evening entry by date."""

  return Evening_Entry.query.filter_by(date=date).first()

def get_am_entry_by_date_range():
  """Return morning entries in a given date range."""

  q = db.session.query(Morning_Entry)
  q = q.filter(Morning_Entry.date >= datetime.date(2021, 5, 5))
  q = q.filter(Morning_Entry.date <= datetime.date(2021, 5, 11))
  q = q.filter(Morning_Entry.user_id==1)
  am_entries = q.all()

  return am_entries

def get_pm_entry_by_date_range():
  """Return evening entries in a given date range."""

  q = db.session.query(Evening_Entry)
  q = q.filter(Evening_Entry.date >= datetime.date(2021, 5, 5))
  q = q.filter(Evening_Entry.date <= datetime.date(2021, 5, 11))
  q = q.filter(Evening_Entry.user_id==1)
  pm_entries = q.all()

  return pm_entries


if __name__ == '__main__':
    from server import app
    connect_to_db(app)