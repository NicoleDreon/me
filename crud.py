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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)