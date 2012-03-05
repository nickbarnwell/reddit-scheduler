import reddit
from ConfigParser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read('config.txt')

username = config.get('user', 'username')
password = config.get('user','password')
user_agent = config.get('client','user_agent')

r = reddit.Reddit(user_agent=user_agent)
r.login(username, password)

BODY_TEXT = '''
WAYWT = What Are You Wearing Today. It doesn't necessarily need to be what you were wearing TODAY.

* Include what the attire is for (work, school, home)
* Pictures are incredibly encouraged as it's quite tough to imagine what someone else is wearing without them.
* **Critiquing others is welcome and encouraged, but keep it constructive/factual.** Take a lesson from Dale Carnegie's [How to Win Friends and Influence People](http://en.wikipedia.org/wiki/How_to_Win_Friends_and_Influence_People) if needed. It takes balls to post pictures of yourself on the Internet, the least you can do is accord the same courtesy as you would to someone in real life.
* [Reddit Enhancement Suite](http://reddit.honestbleeps.com/) makes it very easy to view pictures in a thread.
'''

MONTHS = {
  1:  'Jan.',
  2:  'Feb.',
  3:  'Mar.',
  4:  'Apr',
  5:  'May',
  6:  'June',
  7:  'July',
  8:  'Aug.',
  9:  'Sept.',
  10: 'Oct.',
  11: 'Nov.',
  12: 'Dec.'
}

ENDINGS = {
  0: 'th',
  1: 'st',
  2: 'nd',
  3: 'rd'
}

def get_ending(day):
  if day % 10 in ENDINGS and day not in range(11, 15):
    return ENDINGS[day % 10]
  else:
    return 'th'

def generate_title():
 now = datetime.now()
 month = MONTHS[now.month]
 day = now.day
 ending = get_ending(day)
 return "WAYWT - %(month)s %(day)s%(ending)s" % locals() 
  
r.submit(config.get('reddit','subreddit'), generate_title(), BODY_TEXT)
