"""Models for ME app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime)
    gender = db.Column(db.String)

    def __repr__(self):
        return f'< User user_id = {self.user_id} fname = {self.fname} lname = {self.lname} email = {self.email}, password = {self.password} dob = {self.dob} gender = {self.gender} >'


class Morning_Entry(db.Model):
    """A morning entry."""

    __tablename__ = 'morning_entries'

    am_entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('users.user_id'))
    date = db.Column(db.DateTime, nullable=False)
    hrs_sleep = dbColumn(db.Numeric)
    qual_sleep = db.Column(db.Integer)
    goal = db.Column(db.String)
    journal_entry = db.Column(db.Text)

    def __repr__(self):
        return f'<Morning_Entry user_id={self.user_id} date={self.date} hrs_sleep={self.hrs_sleep} qual_sleep={self.qual_sleep} goal={self.goal} journal_entry={self.journal_entry}>'


class Gratitude(db.Model):
    """A gratitude entry."""

    __tablename__ = 'gratitude'

    gratitude_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    am_entry_id = db.Column(db.Integer, db.ForignKey(
        'morning_entries.am_entry_id'))
    gratitude_entry = db.Column(db.String, nullable=False)
    # should i make reason nullable? would it be text or string if i want to be a short reason one sentance
    gratitude_reason = db.Column(db.Text)

    def __repr__(self):
        return f'<Gratitude gratitude_entry={self.gratitude_entry} gratitude_reason={self.gratitude_reason}>'


class Evening_Entry(db.Model):
    """An evening entry."""

    __tablename__ = 'evening_entries'

    pm_entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('users.user_id'))
    date = db.Column(db.DateTime, nullable=False)
    activity_level = (db.Integer)
    activity = (db.String)
    goal_completed = (db.Boolean, nullable=False)
    # would it be better to call this pm_entry?
    journal_entry = db.Column(db.Text)

    def __repr__(self):
        return f'<Evening_Entry date={self.date} activity_level={self.activity_level} activity={self.activity} goal_completed={self.goal_completed} journal_entry={self.journal_entry}>'


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
