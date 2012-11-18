Reddit Scheduler
---
This script will help to automate the posting of scheduled threads for 
subreddits.

Usage
---

1. `pip install -r requirements.txt` to install the reddit python library

2. Create a file called config.txt in the same directory as the script like so:
    
    [user]
    username: #name
    password: #password

    [reddit]
    subreddit: #subreddit

    [client]
    user_agent: #bot user agent

3. If desired, add the script to your crontab file

4. Run the script and a post should appear per the info supplied in the configuration file


Example configuration info is provided in `postings.json`
