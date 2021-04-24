import requests
import datetime

default_quote = {
  'q': "Today is going to be a good day!",
  'a': None,
  'h': "<blockquote>&ldquo;Today is going to be a good day!</blockquote>"
}

quote_of_the_day = None

quote_of_the_day_last_recieved = None

def get_quote():
  """Get daily quote from zen qoutes api."""
  
  global quote_of_the_day
  global quote_of_the_day_last_recieved

  if quote_of_the_day_last_recieved == None or quote_of_the_day_last_recieved.date() != datetime.datetime.today().date():
    quote_of_the_day = None

  if quote_of_the_day == None:
    res = requests.get('https://zenquotes.io/api/today/')
    if res.status_code == 200:
      quote_of_the_day_last_recieved = datetime.datetime.today()
      quote_of_the_day = res.json()[0]
  
  return quote_of_the_day if quote_of_the_day != None else default_quote