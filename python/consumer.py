import os
import sys
from kafka import KafkaConsumer
import json
from db_table_tweet import create_tables, drop_tables, session, Tweets

drop_tables()

create_tables()

def load_to_db(msg):
    data = msg[6]
    tweets_data = Tweets(
                        id_str=data['id_str'],
                        tweet_id=data['id'],
                        text=data['text'],
                        tweet_created_at=data['created_at'],
                        retweet_count=data['retweet_count'],
                        user_id=data['user']['id'],
                        user_screen_name=data['user']['screen_name'],
                        user_followers_count=data['user']['followers_count'],
                        user_friends_count=data['user']['friends_count']
                         )
    session.merge(tweets_data)
    session.commit()
    session.close()
    print('Loaded data')


consumer = KafkaConsumer('vache', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for msg in consumer:
    load_to_db(msg)



'''
 if __name__=='__main__':
    create_tables()
    c = Consumer({
        'bootstrap.servers': 'localhost:9092,localhost:9093',
        'auto.offset.reset': 'earliest'
    })
    c.subscribe(['woocommerce'])
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        load_to_db(msg)
    c.close()
'''