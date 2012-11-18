import reddit
import json
from ConfigParser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read('config.txt')

username = config.get('user', 'username')
password = config.get('user','password')
user_agent = config.get('client','user_agent')

posts = json.loads(open('postings.json','r').read())

r = reddit.Reddit(user_agent=user_agent)
r.login(username, password)

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

def generate_title(title):
 now = datetime.now()
 month = MONTHS[now.month]
 day = now.day
 ending = get_ending(day)
 return "%(title)s - %(month)s %(day)s%(ending)s" % locals() 

if __name__ == '__main__':
  weekday = datetime.now().weekday()
  for post in posts:
    if weekday in post['day']:
      title = post['title']
      with open('bodies/%s.txt' % title) as f:
        print "Posting %s" % (generate_title(title))
        item = r.submit(config.get('reddit','subreddit'),
                 generate_title(title),
                 f.read()
                )
        item.distinguish() #FIXME(nickbarnwell): This should be in config
        item.set_flair(post['flair'], post['class'])
