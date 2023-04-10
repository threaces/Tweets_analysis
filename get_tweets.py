import snscrape.modules.twitter as sntwitter
import pandas as pd
import pprint
from queries import list_queries
import time


def get_raw_data_scraper(query):
    
    tweets = []
    limit = 1500

   
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            
        if len(tweets) == limit:
            break
        else:
            dict_of_tweet_info = {}
            dict_of_tweet_info['Date of Creation'] = tweet.date
            dict_of_tweet_info['Content'] = tweet.rawContent
            #dict_of_tweet_info['Location'] = tweet.location
            dict_of_tweet_info['hashtags'] = tweet.hashtags
            dict_of_tweet_info['User'] = tweet.user.username
            tweets.append(dict_of_tweet_info)

    return tweets

def get_raw_df():
    '''list_of_tweets = []

    for item in list_queries:
        one_element = get_raw_data_scraper(item)
        list_of_tweets.append(one_element)'''

    raw_df = pd.DataFrame.from_records(get_raw_data_scraper(list_queries[-1]))

    return raw_df

def get_csv_file():
    
    df = get_raw_df()

    df.to_csv('Raw_database_tweets_arsenal_10_04_2023.csv', na_rep='N/A', mode='a')

start_time = time.time()
pprint.pprint(get_csv_file())
print(f"Czas pracy: {time.time() - start_time}")



    