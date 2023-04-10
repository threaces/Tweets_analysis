from pymongo import MongoClient

url_database = 'mongodb+srv://popekwot:OLtdw08tUq6u0ddD@mycluster.0zmakdn.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(url_database)

dbname = client
concrete_db = dbname['Premier_league_tweets']
collection = concrete_db['Arsenal_tweets']

for tweet in collection.find({'Tweet.Date': '2023-03-19'}):
    print(tweet)
    