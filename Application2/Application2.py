
#Brief: Sentiment analysis. It is the understaing and extracting feelings from data.
# How this work is by tokenization and other algorithms.Tokenization is breaking a sentence into smaller parts. 
#For example, Subject, object and verb. Then the algorithm checks the number of tokenized words against the sentiment lexicon. 
#In this case i'll be using tweepy, which is a library that could be used to access twitter API.Textblob is the library that does the analysis.

import tweepy
from textblob import TextBlob
import csv

APIKey              = "hbUbiPytE7sJBXkOPvcckzxcO"
APISecretKey        = "B9I2b1mZ0pDaGfqBvpU3qXM1Szh8pl1Fyjmg4s7fSSR18RCR5c"
accessToken         = "250077812-RMy1LsoHL5ZsIoE7MruuSWNoxzg0kgO1whkA0eV5"
accessTokenSecret   = "Acttx01JhEtwiDQ5CwkMqOEd1b0JyHbyMMLC9aFKsWfrZ"

authenticate    = tweepy.OAuthHandler(APIKey,APISecretKey) 
authenticate.set_access_token(accessToken, accessTokenSecret) 

API = tweepy.API(authenticate) #Authenticating with the Twitter API 

print("Welcome to Twitter Sentiment Analysis")
sentimentSearch = input("Type the text you would like to search : ").encode("utf-8")
print("\n")
tweets = API.search(sentimentSearch)
with open("TwitterSentimentAnalysis.csv", 'w', newline="") as TSA:
     csvwriter = csv.writer(TSA)
     csvwriter.writerow(["UserName","Tweet","Sentiment"])

     for tweet in tweets:
        analysis = TextBlob(tweet.text)
        csvwriter.writerow([tweet.user.screen_name, tweet.text, analysis.sentiment])



    


