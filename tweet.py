from snscrape.modules.twitter import TwitterUserScraper
import pandas as pd
user = 'tonybenoy'
list_tweets = []
count = 1000 # Use a date logic in loop instead of count
tweets = TwitterUserScraper(user).get_items()
for tweet in tweets:
    print(tweet.json())
    list_tweets.append(tweet.json()) # Refer here for all possible values https://thetechrobo.ca/snscrape-docs/_autosummary/snscrape.modules.twitter.Tweet.html#snscrape.modules.twitter.Tweet
    count -= 1
    if count == 0: # Use a date logic in loop instead of count
        break
df = pd.DataFrame(list_tweets)
df.to_csv('tweets.csv', index=False)