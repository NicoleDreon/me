"""Models for ME app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime)
    gender = db.Column(db.String)

    def __repr__(self):
        return f'< User user_id = {self.user_id} fname = {self.fname} lname = {self.lname} email = {self.email}, phone={self.phone} password = {self.password} dob = {self.dob} gender = {self.gender} >'

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
        }
       


class Morning_Entry(db.Model):
    """A morning entry."""

    __tablename__ = 'morning_entries'

    am_entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    hrs_sleep = db.Column(db.Numeric)
    qual_sleep = db.Column(db.Integer)
    snooze = db.Column(db.Integer)
    goal = db.Column(db.String)
    journal_entry = db.Column(db.Text)

    def __repr__(self):
        return f'<Morning_Entry user_id={self.user_id} date={self.date} hrs_sleep={self.hrs_sleep} qual_sleep={self.qual_sleep} snooze={self.snooze} goal={self.goal} journal_entry={self.journal_entry}>'

    user = db.relationship('User', backref='morning_entries')

class Gratitude(db.Model):
    """A gratitude entry."""

    __tablename__ = 'gratitude'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    am_entry_id = db.Column(db.Integer, db.ForeignKey(
        'morning_entries.am_entry_id'))
    entry = db.Column(db.String, nullable=False)
    reason = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Gratitude entry={self.entry} reason={self.reason}>'

    morning_entries = db.relationship('Morning_Entry', backref='gratitudes')

class Evening_Entry(db.Model):
    """An evening entry."""

    __tablename__ = 'evening_entries'

    pm_entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date = db.Column(db.DateTime, nullable=False)
    activity_level = db.Column(db.Integer)
    activity = db.Column(db.String)
    goal_completed = db.Column(db.Boolean)
    qual_day = db.Column(db.Integer, nullable=False)
    journal_entry = db.Column(db.Text)

    def __repr__(self):
        return f'<Evening_Entry pm_entry_id={self.pm_entry_id} date={self.date} activity_level={self.activity_level} activity={self.activity} goal_completed={self.goal_completed} journal_entry={self.journal_entry}>'

    user = db.relationship('User', backref='evening_entries')

class Emotion_Entry(db.Model):
    """An emotion entry."""

    __tablename__ = 'emotion_entries'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pm_entry_id = db.Column(db.Integer, db.ForeignKey('evening_entries.pm_entry_id'))
    emotion_id = db.Column(db.Integer, db.ForeignKey('emotions.id'))

    def __repr__(self):
        return f'<Emotion emotion{self.emotion}>'

    evening_entry = db.relationship('Evening_Entry', backref='emotion_entries')
    emotion = db.relationship('Emotion', backref='emotion_entries')
   

class Emotion(db.Model):
    """An emotion."""

    __tablename__ = 'emotions'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    emotion = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<Emotion emotion={self.emotion} user_id={self.user_id}>'

    user = db.relationship('User', backref='emotions')

def connect_to_db(flask_app, db_uri='postgresql:///entries', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
