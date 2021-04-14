"""Populate database."""
import server
import os
from datetime import datetime

from model import db, User, Morning_Entry, Gratitude, Evening_Entry, Emotion_Entry, Emotion, connect_to_db
os.system('dropdb entries')
os.system('createdb entries')
connect_to_db(server.app)

db.create_all()
  

# def seed():
  # create test users
user1 = User(fname='Noelle', lname='Smith',
                  email='noelle@gmail.com', password='letsdothis', dob='09-12-1982', gender='Female')
user2 = User(fname='Nicole', lname='Dreon',
                  email='nicole@yahoo.com', password='sunshine', dob='08-28-1985', gender='Female')
user3 = User(fname='Brian', lname='Roberts',
                  email='broberts@gmail.com', password='music', dob='12-17-1990', gender='Male')
user4 = User(fname='Skylar', lname='Jones', email='skylerjones@mail.com',
                  password='password', dob='04-18-2001', gender='non-bianary')

  # create test am_entries
user1_am_entry1 = Morning_Entry(user_id=1, date='04-06-2021', hrs_sleep=7, qual_sleep=9, goal='Meet with mentor', journal_entry='Ready for today!')

user1_am_entry2 = Morning_Entry(user_id=1, date='04-07-2021', hrs_sleep=8.5, qual_sleep=8, goal='Seed my db', journal_entry='It is a beautiful day!')

user2_am_entry1 = Morning_Entry(user_id=2, date='04-07-2021', hrs_sleep=8, qual_sleep=8, goal='Go for a walk', journal_entry='I can do this!')

  # create gratitude entries
user1_gratitude1 = Gratitude(am_entry_id=1, entry='The sun', reason='It warms my soul')

user1_gratitude2 = Gratitude(am_entry_id=1, entry='My bed', reason='It supports me while I sleep')

user1_gratitude3 = Gratitude(am_entry_id=1, entry='Thu', reason='Shes great at explaning code and concepts')

  # create evening entries
user1_evening_entry1 = Evening_Entry(user_id=1, date='04-06-2021', activity_level=7, activity='walking', goal_completed=True, 
  qual_day=8, journal_entry='What a long day! Made progress on my project. The highlight of my day was spending time with my husband and kids.')

user1_evening_entry2 = Evening_Entry(user_id=1, date='04-07-2021', activity_level=4, activity='does coding count?', goal_completed=False, qual_day=10, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user2_evening_entry1 = Evening_Entry(user_id=2, date='04-07-2021', activity_level=7, activity='soccer', goal_completed=True, qual_day= 7, journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

  # create emotion entries
user1_emotion1 = Emotion_Entry(pm_entry_id=1, emotion_id=2)
user1_emotion2 = Emotion_Entry(pm_entry_id=1, emotion_id=3)
user1_emotion3 = Emotion_Entry(pm_entry_id=1, emotion_id=4)

  # create emotions
sad = Emotion(emotion='Sad')
happy = Emotion(emotion='Happy')
joy = Emotion(emotion='Joy')
tired = Emotion(emotion='tired')

  # db.session.add(am_entry1)
db.session.add_all([user1, user2, user3, user4, user1_am_entry1, user1_am_entry2, user2_am_entry1, user1_gratitude1, user1_gratitude2, user1_gratitude3, user1_evening_entry1, user1_evening_entry2, user2_evening_entry1, sad, happy, joy, tired])
db.session.commit()

# if __name__ == '__main__':
    
   

# find user by name
# User.query.filter_by(fname='Name')

# connect user to am entry
# db.session.query(User, Morning_Entry).join(Morning_Entry).all()

# connect user to pm entry

# connnect emotion to emotion entry

# connect emotion entry to pm entry

# connect gratitude to am entry

# get journal entries by user

# get email and password from user for login
# users = db.session.query(User).all()
# for user in users:
#   print(user.email, user.password);

# join user to emotion table
# db.session.query(User, Emotion).outerjoin(Emotion).all()


# user = db.session.query(User).filter_by(user_id=1).one()
# user.evening_entries
# user.morning_entries
# user.emotions





