import requests

default_quote = [
  {
  'q': "Today is going to be a good day!",
  'a': None,
  'h': "<blockquote>&ldquo;Today is going to be a good day!</blockquote>"
}
]
# <blockquote>&ldquo;Be where your enemy is not.&rdquo; &mdash; <footer>Sun Tzu</footer></blockquote>

def get_quote():
  """Get quote from zen qoutes api."""
  res = requests.get('https://zenquotes.io/api/today/')

  return res.json() if res.status_code == 200 else default_quote

  # res.json()
  # if res.status_code == 200:
  #   return res

  # else: 
  #   return "Today is going to be a good day!"