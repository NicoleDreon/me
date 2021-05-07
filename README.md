# Mindful Everyday

In the modern world we’re constantly inundated by external stimuli, carefully curated to hold our attention and direct our actions. With these distractions it becomes more challenging to go inward. Journaling has always been a great tool. However unless you go back through all your old entries it's hard to see any correlation. Mindful Everyday was created to bridge that gap. It’s a space for users to slow down, take time for themselves each day, and visually see trends in their daily practices.

## Tech Stack

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

## Demo

Insert gif or link to demo

## Features

### Landing Page

Already existing users can log in.

![landing page](https://github.com/NicoleDreon/me/blob/main/static/landing.png)

Or a new user can register.

![create account](https://github.com/NicoleDreon/me/blob/main/static/signup.png)

### Past Entries/User Homepage

Once logged in the user will be directd to their hompage which displays all their past journal entries. The daily inspiration quote is being pulled in from the Zen Quotes API.

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

### Analytics

All the users quantifiable data is gatehered and dispalyed using Chart.js. Users can turn on and off lines on the graph (by clicking the key) to explore possible correlations.

![chart](https://github.com/NicoleDreon/me/blob/main/static/chart.png)

### Profile

A snapshot of the users data.

![profile card](https://github.com/NicoleDreon/me/blob/main/static/profile.png)

## Documentation

[Documentation](https://linktodocumentation)

## License

[MIT](https://choosealicense.com/licenses/mit/)
