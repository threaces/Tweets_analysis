from pymongo import MongoClient
import datetime
from nlp_arsenal import sentiment_analysis

def get_database():

    url_database = 'mongodb+srv://popekwot:OLtdw08tUq6u0ddD@mycluster.0zmakdn.mongodb.net/?retryWrites=true&w=majority'

    client = MongoClient(url_database, serverSelectionTimeoutMS = 6000000)

    return client

dbname = get_database()
concrete_db = dbname['Premier_league_tweets']
collection = concrete_db['Arsenal_tweets']
list_of_dict = sentiment_analysis()
collection.insert_many(list_of_dict[0:])
