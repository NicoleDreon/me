"""Populate database."""
import server
import os

from model import db, User, Morning_Entry, Gratitude, Evening_Entry, Emotion_Entry, Emotion, connect_to_db

os.system('dropdb entries')
os.system('createdb entries')

connect_to_db(server.app)
db.create_all()
  

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
user1_am_entry1 = Morning_Entry(user_id=1, date='04-28-2021', hrs_sleep=7, qual_sleep=4, snooze= 2, goal='Meet with mentor', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor purus non enim praesent elementum facilisis leo vel. Turpis massa sed elementum tempus egestas. Lacus luctus accumsan tortor posuere ac ut. Neque gravida in fermentum et sollicitudin ac orci phasellus egestas. Porta non pulvinar neque laoreet suspendisse interdum consectetur. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Scelerisque mauris pellentesque pulvinar pellentesque. Quis ipsum suspendisse ultrices gravida dictum fusce ut. Mauris pellentesque pulvinar pellentesque habitant. Nisl tincidunt eget nullam non nisi est sit amet. Diam donec adipiscing tristique risus nec feugiat in.')

user1_am_entry2 = Morning_Entry(user_id=1, date='04-29-2021', hrs_sleep=8.5, qual_sleep=5,snooze=1, goal='Seed my db', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor purus non enim praesent elementum facilisis leo vel. Turpis massa sed elementum tempus egestas. Lacus luctus accumsan tortor posuere ac ut. Neque gravida in fermentum et sollicitudin ac orci phasellus egestas. Porta non pulvinar neque laoreet suspendisse interdum consectetur. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Scelerisque mauris pellentesque pulvinar pellentesque. Quis ipsum suspendisse ultrices gravida dictum fusce ut. Mauris pellentesque pulvinar pellentesque habitant. Nisl tincidunt eget nullam non nisi est sit amet. Diam donec adipiscing tristique risus nec feugiat in.')

user1_am_entry3 = Morning_Entry(user_id=1, date='04-30-2021', hrs_sleep=8, qual_sleep=4,snooze=1, goal='Go for a run', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit. ')

user1_am_entry4 = Morning_Entry(user_id=1, date='05-01-2021', hrs_sleep=8.5, qual_sleep=3,snooze=1, goal='Wash clothes', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Gravida rutrum quisque non tellus orci ac auctor augue mauris. A iaculis at erat pellentesque adipiscing commodo elit at. Congue eu consequat ac felis donec et odio. Volutpat odio facilisis mauris sit amet massa vitae tortor condimentum. Sagittis id consectetur purus ut faucibus pulvinar elementum integer. Scelerisque purus semper eget duis at tellus at urna. Ullamcorper morbi tincidunt ornare massa. Non arcu risus quis varius quam quisque id diam. Libero volutpat sed cras ornare arcu dui vivamus arcu felis. Massa ultricies mi quis hendrerit dolor magna.')

user1_am_entry5 = Morning_Entry(user_id=1, date='05-02-2021', hrs_sleep=9, qual_sleep=5,snooze=0, goal='Grocery shopping', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit. ')

user1_am_entry6 = Morning_Entry(user_id=1, date='05-03-2021', hrs_sleep=8.5, qual_sleep=3,snooze=1, goal='Seed my db', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Gravida rutrum quisque non tellus orci ac auctor augue mauris. A iaculis at erat pellentesque adipiscing commodo elit at. Congue eu consequat ac felis donec et odio. Volutpat odio facilisis mauris sit amet massa vitae tortor condimentum. Sagittis id consectetur purus ut faucibus pulvinar elementum integer. Scelerisque purus semper eget duis at tellus at urna. Ullamcorper morbi tincidunt ornare massa. Non arcu risus quis varius quam quisque id diam. Libero volutpat sed cras ornare arcu dui vivamus arcu felis. Massa ultricies mi quis hendrerit dolor magna. \nNeque ornare aenean euismod elementum nisi quis. Fames ac turpis egestas integer eget aliquet nibh praesent tristique. Tortor consequat id porta nibh venenatis cras sed. Ipsum dolor sit amet consectetur adipiscing elit duis tristique. Nam at lectus urna duis convallis. Condimentum vitae sapien pellentesque habitant morbi tristique. Amet consectetur adipiscing elit ut aliquam purus. Tempor nec feugiat nisl pretium fusce id velit. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Vestibulum sed arcu non odio euismod. Tortor at auctor urna nunc id cursus metus aliquam eleifend. Diam donec adipiscing tristique risus nec feugiat. In nibh mauris cursus mattis molestie a iaculis at. Lacus sed turpis tincidunt id aliquet risus feugiat in. Mattis vulputate enim nulla aliquet porttitor lacus. Aliquam id diam maecenas ultricies mi. \nCras semper auctor neque vitae. Purus semper eget duis at tellus at urna condimentum. Velit laoreet id donec ultrices tincidunt. Sit amet venenatis urna cursus eget nunc scelerisque. Suspendisse interdum consectetur libero id faucibus nisl tincidunt eget nullam. Massa sed elementum tempus egestas sed. Aenean euismod elementum nisi quis eleifend quam. Id faucibus nisl tincidunt eget nullam. Nulla pharetra diam sit amet nisl suscipit. Faucibus purus in massa tempor nec feugiat. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et. Proin libero nunc consequat interdum varius sit amet. Egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices. Aliquam sem fringilla ut morbi tincidunt. Semper auctor neque vitae tempus. Mattis ullamcorper velit sed ullamcorper morbi. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Amet risus nullam eget felis.')

user1_am_entry7 = Morning_Entry(user_id=1, date='05-04-2021', hrs_sleep=6.5, qual_sleep=3,snooze=3, goal='Seed my db', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor purus non enim praesent elementum facilisis leo vel. Turpis massa sed elementum tempus egestas. Lacus luctus accumsan tortor posuere ac ut. Neque gravida in fermentum et sollicitudin ac orci phasellus egestas. Porta non pulvinar neque laoreet suspendisse interdum consectetur. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Scelerisque mauris pellentesque pulvinar pellentesque. Quis ipsum suspendisse ultrices gravida dictum fusce ut. Mauris pellentesque pulvinar pellentesque habitant. Nisl tincidunt eget nullam non nisi est sit amet. Diam donec adipiscing tristique risus nec feugiat in.')

user2_am_entry1 = Morning_Entry(user_id=2, date='04-07-2021', hrs_sleep=8, qual_sleep=8, snooze=0, goal='Go for a walk', journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit. Suspendisse potenti nullam ac tortor vitae purus faucibus. Dui faucibus in ornare quam viverra orci. Sed faucibus turpis in eu mi bibendum neque egestas congue. Elementum nisi quis eleifend quam adipiscing. Fringilla est ullamcorper eget nulla. Sed velit dignissim sodales ut. Nulla aliquet enim tortor at. Sed tempus urna et pharetra pharetra.')

  # create gratitude entries
user1_gratitude1 = Gratitude(am_entry_id=1, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude2 = Gratitude(am_entry_id=1, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude3 = Gratitude(am_entry_id=1, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude4 = Gratitude(am_entry_id=2, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude5 = Gratitude(am_entry_id=2, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude6 = Gratitude(am_entry_id=2, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude7 = Gratitude(am_entry_id=3, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude8 = Gratitude(am_entry_id=3, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude9 = Gratitude(am_entry_id=3, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude10 = Gratitude(am_entry_id=4, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude11 = Gratitude(am_entry_id=4, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude12 = Gratitude(am_entry_id=4, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude13 = Gratitude(am_entry_id=5, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude14 = Gratitude(am_entry_id=5, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude15 = Gratitude(am_entry_id=5, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude16 = Gratitude(am_entry_id=6, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude17 = Gratitude(am_entry_id=6, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude18 = Gratitude(am_entry_id=6, entry='Lorem ipsum', reason='Lorem ipsum dolor sit amet')

user1_gratitude19 = Gratitude(am_entry_id=7, entry='The sun', reason='It warms my soul')

user1_gratitude20 = Gratitude(am_entry_id=7, entry='My bed', reason='It supports me while I sleep')

user1_gratitude21 = Gratitude(am_entry_id=7, entry='Thu', reason='She is great at explaning code and concepts')

  # create evening entries
user1_evening_entry1 = Evening_Entry(user_id=1, date='04-28-2021', activity_level=5, activity='walking', goal_completed=True, 
  qual_day=4, journal_entry='What a long day! Made progress on my project. The highlight of my day was spending time with my husband and kids.')

user1_evening_entry2 = Evening_Entry(user_id=1, date='04-29-2021', activity_level=4, activity='does coding count?', goal_completed=False, qual_day=3, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user1_evening_entry3 = Evening_Entry(user_id=1, date='04-30-2021', activity_level=4, activity='does coding count?', goal_completed=False, qual_day=5, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user1_evening_entry4 = Evening_Entry(user_id=1, date='05-01-2021', activity_level=4, activity='does coding count?', goal_completed=True, qual_day=4, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user1_evening_entry5 = Evening_Entry(user_id=1, date='05-02-2021', activity_level=4, activity='does coding count?', goal_completed=True, qual_day=4, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user1_evening_entry6 = Evening_Entry(user_id=1, date='05-03-2021', activity_level=4, activity='does coding count?', goal_completed=False, qual_day=5, journal_entry='So much time on the computer today. Very productive but no time for lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

user1_evening_entry7 = Evening_Entry(user_id=1, date='05-04-2021', activity_level=4, activity='does coding count?', goal_completed=False, qual_day=2, journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Gravida rutrum quisque non tellus orci ac auctor augue mauris. A iaculis at erat pellentesque adipiscing commodo elit at. Congue eu consequat ac felis donec et odio. Volutpat odio facilisis mauris sit amet massa vitae tortor condimentum. Sagittis id consectetur purus ut faucibus pulvinar elementum integer. Scelerisque purus semper eget duis at tellus at urna. Ullamcorper morbi tincidunt ornare massa. Non arcu risus quis varius quam quisque id diam. Libero volutpat sed cras ornare arcu dui vivamus arcu felis. Massa ultricies mi quis hendrerit dolor magna.')

user2_evening_entry1 = Evening_Entry(user_id=2, date='05-04-2021', activity_level=7, activity='soccer', goal_completed=True, qual_day= 7, journal_entry='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

  # create emotions
sad = Emotion(emotion='Sad')
happy = Emotion(emotion='Happy')
joy = Emotion(emotion='Joy')
tired = Emotion(emotion='tired')

  # create emotion entries
user1_emotion1 = Emotion_Entry(pm_entry_id=1, emotion_id=2)
user1_emotion2 = Emotion_Entry(pm_entry_id=1, emotion_id=3)
user1_emotion3 = Emotion_Entry(pm_entry_id=1, emotion_id=4)

  # db.session.add(am_entry1)
db.session.add_all([user1, user2, user3, user4, user1_am_entry1, user1_am_entry2, user1_am_entry3, user1_am_entry4, user1_am_entry5, user1_am_entry6, user1_am_entry7, user2_am_entry1, user1_gratitude1, user1_gratitude2, user1_gratitude3, user1_gratitude4, user1_gratitude5, user1_gratitude6, user1_gratitude7, user1_gratitude8, user1_gratitude9, user1_gratitude10, user1_gratitude11, user1_gratitude12, user1_gratitude13, user1_gratitude14, user1_gratitude15, user1_gratitude16, user1_gratitude16, user1_gratitude17, user1_gratitude18, user1_gratitude19, user1_gratitude20, user1_gratitude21, user1_evening_entry1, user1_evening_entry2, user1_evening_entry3, user1_evening_entry4, user1_evening_entry5, user1_evening_entry6, user1_evening_entry7, user2_evening_entry1, sad, happy, joy, tired, user1_emotion1, user1_emotion2, user1_emotion3])
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

# test = db.session.query(User).filter_by(user_id = 1).one()
# am = test_user.morning_entries
# for entry in am:
#   gratitudes = entry.gratitudes
#   for gratitude in gratitudes:
#     print(gratitude.entry)
#     print(gratitude.reason)

# test = db.session.query(User).filter_by(user_id = 1).all()
# test = test.morning_entries
# for x in test:
    # for y in test.gratitudes:
    #   print(y)
    # print(x)

# write in crud
# call in server in past_entries route
# jinja to display
