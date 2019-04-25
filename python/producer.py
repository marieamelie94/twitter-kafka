from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = "##"
access_token_secret =  "##"
consumer_key =  "##"
consumer_secret =  "##"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("un", data.encode('utf-8'))
        print(data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="ulyse nardin")

#-----------------------------------------------------------
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient, KafkaProducer


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("un", data.encode('utf-8'))
        print(data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = KafkaProducer(kafka)
listener = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)
stream.filter(track="ulyse nardin")


#--------------------------------------------------version 2

from kafka import KafkaProducer
import twitter

twapi = twitter.Api(
    consumer_key = " ",
    consumer_secret = " ",
    access_token_key = " ",
    access_token_secret = " "
    )

response = ''

response = twapi.GetSearch(raw_query='q="ulysse nardin"&since=2019-02-01&until=2019-04-25')

#---------------------
response = twapi.GetSearch(raw_query='q="notre dame"&result_type=popular&since=2019-04-01&count=100')


producer = KafkaProducer(bootstrap_servers='localhost:9092')
    for i in range(200):
        producer.send('un', response[i])