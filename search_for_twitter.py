import snscrape.modules.twitter as sntwitter 
import pandas as pd 
from time import sleep 

tweet_data = [] 
username = input('Enter your keyword: ')
number = int(input('How many tweets do you want to scrape: ')) 
for i, tweets in enumerate(sntwitter.TwitterHashtagScraper('{}'.format(username)).get_items()):
    if i > number:
        break 
    tweet_data.append([tweets.date, tweets.content, tweets.user.username ])
                                                      
df = pd.DataFrame(tweet_data, columns=['Date','Tweets','Username'])



############## for emails ##############

#Convert to Dataframe 
df = pd.DataFrame(tweet_data,columns=['Date','Tweets','Username'])

#Extract mails containing
emails=df[df['Tweets'].str.contains('@')]


import re
def find_email(text):
    email = re.findall('\S+@\S+', str(text))
    return ",".join(email)

email_only=list(emails['Tweets'].apply(lambda x: find_email(x)))
Email=pd.DataFrame(email_only,columns=['Emails']).dropna().drop_duplicates()
print(Email)


