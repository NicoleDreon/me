# Mindful Everyday

In the modern world we’re constantly inundated by external stimuli, carefully curated to hold our attention and direct our actions. With these distractions it becomes more challenging to go inward. Journaling has always been a great tool. However unless you go back through all your old entries it's hard to see any correlation. Mindful Everyday was created to bridge that gap. It’s a space for users to slow down, take time for themselves each day, and visually see trends in their daily practices.

## Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Documentation](#documentation)
- [Future State](#future)
- [Installation](#installation)

## <a name="tech-stack"></a>Tech Stack

- Python
- JavaScript
- HTML
- CSS
- Bootstrap
- Flask
- Jinja
- PostgreSQL
- SQLAlchemy
- Chart.js

<!-- ## Demo

Insert gif or link to demo -->

## <a name="features"></a>Features

### Landing Page

Already existing users can log in.

![landing page](https://github.com/NicoleDreon/me/blob/main/static/landing.png)

Or a new user can register. Once a new user is added they will be redirected to their [profile](#profile) page.

![create account](https://github.com/NicoleDreon/me/blob/main/static/signup.png)

### Past Entries/User Homepage

Once logged in the user is directd to their hompage which displays all their past journal entries and a daily inspirational quote which is being pulled in from the Zen Quotes API.

![past entry with quote](https://github.com/NicoleDreon/me/blob/main/static/past_entry.png)

Each day is displayed in a past entry card with links together the morning and evening entries into one card using a jinja for loop.

![past entry card](https://github.com/NicoleDreon/me/blob/main/static/entry_card.png)

### New Entry

A user can make a new morning or evening entry from any page by selecting the option in the navbar. Once submitted the user will be redirected to their past entries where the new entry will be added in chronological order.

![new entry](https://github.com/NicoleDreon/me/blob/main/static/new_entry.png)

Add a new morning entry

![new morning entry](https://github.com/NicoleDreon/me/blob/main/static/am_entry.png)

Add a new evening entry

![new evening entry](https://github.com/NicoleDreon/me/blob/main/static/pm_entry.png)

If the user tries to make either a morning entry or evening entry on a day that they already have and entry for that time of day a JavaScript alert will appear to notify the user an entry already exists.

![new evening entry](https://github.com/NicoleDreon/me/blob/main/static/alert.png)

### Analytics

All the users quantifiable data is gatehered and dispalyed using Chart.js. Users can turn on and off lines on the graph (by clicking the key) to explore possible correlations.

![chart](https://github.com/NicoleDreon/me/blob/main/static/chart.png)

### <a name="profile"></a>Profile

A snapshot of the users data.

![profile card](https://github.com/NicoleDreon/me/blob/main/static/profile.png)

## <a name="future"></a>Future State

Future goals for Mindful Everyday

- Analytics
  - Option to choose 7 day range
  - Chart for month and year
- Calender/search bar to filter past entries
- Badges or counter to track number of days in a row entries were made

## <a name="installation"></a>Installation

Run Mindful Everyday on your own machine.

- Install PostgreSQL (Mac OSX)

- Clone or fork this repo:

```
https://github.com/NicoleDreon/me.git
```

- Create and activate a virtual environment inside your Mindful Everyday directory:

```
virtualenv env
source env/bin/activate
```

- Install dependencies:

```
pip install -r requirements.txt
```

- Set up database:

```
createdb entries
python3 model.py
```

- Run the app:

```
python3.6 server.py
```

- Navigate to 'localhost:5000/' to access Mindful Everyday and start journaling!

<!-- ## License

[MIT](https://choosealicense.com/licenses/mit/) -->

Copyright (c) [2020] [Nicole Dreon]
