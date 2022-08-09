import os
import json_normalize
import dtale
import pandas as pd
filname="/home/bilgi/Desktop/zyzy.csv"
filname2="/home/bilgi/Desktop/zyzy.csv"
raw_tweets = pd.read_json(filname, lines=True, encoding='utf-8')
raw_tweets.to_csv(filname2,index=None)
# users = json_normalize(raw_tweets)
# users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
# users.rename(columns={'id': 'userId', 'url': 'profileUrl'}, inplace=True)
# # Create DataFrame and remove duplicates
# users = pd.DataFrame(users)
# # users.drop_duplicates(subset=['userId'], inplace=True)
# # Transform 'raw_tweets' DataFrame
# # Add column for 'userId'
# user_id = [user['id'] for user in raw_tweets['user']]
# raw_tweets['userId'] = user_id
# # Remove less important columns
# cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount',
#         'quoteCount']
# tweets = raw_tweets[cols]
# tweets.rename(columns={'id': 'tweetId', 'url': 'tweetUrl'}, inplace=True)
# cols = ['username', 'userId', 'displayname', 'followersCount', 'friendsCount', 'favouritesCount',
#         'location']
# use = users[cols]
# twts = use.merge(tweets, on='userId')
# twts.to_csv(filname, index=False)
# # tweets_df4.to_csv(filname4 ,index=False)
# result4 = "successfully completed with {} results".format(len(twts))
# print(result4)
df = pd.read_csv(filname2)
d = dtale.show(df)
d.open_browser()