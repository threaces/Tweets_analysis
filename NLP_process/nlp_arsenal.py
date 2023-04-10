from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import pandas as pd
import datetime
import numpy

# Load a raw database of tweets

raw_df = pd.read_csv('E:\data_science_pierwsze_Lekcje\Twitter_pl_club_tweets\Raw_database_tweets_arsenal_10_04_2023.csv')
raw_df = raw_df.drop("Unnamed: 0", axis=1)

# get a list of dates
list_of_dates = []

for row, values in raw_df.iterrows():
    date = values[0][0: 10]
    
    if date not in list_of_dates:
        list_of_dates.append(date)
    
    break

def list_tweets_day(date):
    list_of_tweets_day = []

    for row, values in raw_df.iterrows():
        if date in values[0]:
            list_of_tweets_day.append(values[1])

    return list_of_tweets_day

list_of_tweets = list_tweets_day(list_of_dates[0])
#list_of_tweets = raw_df['Content'].to_list()

# preprocess tweets

tweets_words = []

for item in list_of_tweets:

    one_tweet = []

    for word in item.split(" "):
        word = word.replace('\n', "")
        if word.startswith("@") and len(word) > 1:
            word = '@user'
        elif word.startswith("http"):
            word = 'http'
        one_tweet.append(word)

    tweets_words.append(one_tweet)

modified_tweets = []

for item in tweets_words:
    tweet_process = " ".join(item)
    modified_tweets.append(tweet_process)

roberta = 'cardiffnlp/twitter-roberta-base-sentiment'

model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis

def sentiment_analysis():

    list_of_dictionaries = []

    for item in modified_tweets:
        dict_element = {}
        encoded_tweet = tokenizer(item, return_tensors='pt')
        output = model(**encoded_tweet)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        sentiment_dict = {}

        for i in range(len(scores)):
            
            l = labels[i]
            s = scores[i]
            
            sentiment_dict[l] = float(s)
            
        dict_element['Tweet'] = {"Content" : item, "Sentiment Result" : sentiment_dict, "Date": list_of_dates[0]}
        list_of_dictionaries.append(dict_element)
        
    return list_of_dictionaries

call_sentiment_function = sentiment_analysis()
        