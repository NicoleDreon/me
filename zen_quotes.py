import requests

default_quote = {
  'q': "Today is going to be a good day!",
  'a': None,
  'h': "<blockquote>&ldquo;Today is going to be a good day!</blockquote>"
}

quote_of_the_day = None

# <blockquote>&ldquo;Be where your enemy is not.&rdquo; &mdash; <footer>Sun Tzu</footer></blockquote>

def get_quote():
  """Get quote from zen qoutes api."""
  # could grab random quote each time page 
  
  global quote_of_the_day
  if quote_of_the_day == None:
    res = requests.get('https://zenquotes.io/api/today/')
    quote_of_the_day = res.json()[0] if res.status_code == 200 else None
  
  
  return quote_of_the_day if quote_of_the_day != None else default_quote

  # res.json()
  # if res.status_code == 200:
  #   return res

  # else: 
  #   return "Today is going to be a good day!"