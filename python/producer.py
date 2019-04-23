from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import Producer, KafkaClient

access_token = "1118901487474827264-93TjqBwfgpsEpbmhgzFB6bS6hNFrKh"
access_token_secret =  "7k4tPE7bl7XZBZQvhtxxfVdIcEDnzploPk2Z0nGoM6v2t"
consumer_key =  "zOyHjlMIoX5848c4BqncbmwiX"
consumer_secret =  "g8WGS31OREfNPX1RosAocyH5lshzV6NFoImdSy3znEMwC8MV19"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("cow", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="cow")

