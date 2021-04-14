"""CRUD operations."""

from model import db, User, Morning_Entry, Gratitude, Evening_Entry, Emotion_Entry, Emotion, connect_to_db

def check_login(email):
  """Check if user exists in db."""
    
  return User.query.filter_by(email=email).first()

def get_user(user_id):
  """Return user by id."""

  return User.query.filter_by(user_id=user_id).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)