"""CRUD operations."""

from model import db, User, Morning_Entry, Gratitude, Evening_Entry, Emotion_Entry, Emotion, connect_to_db

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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)