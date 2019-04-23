import os
import sys

#sys.path.append(os.path.join('/home/marie_montredo/data-pipeline-python-kafka'))

import db_connection as db
from sqlalchemy import Column, String, Date, Numeric, DateTime, BigInteger


con_yml_dict = {
    'db_user': 'postgresuser' ,
    'db_passwd': 'postgrespassword',
    'db_name': 'main',
    'db_host': 'localhost',
    'db_port': '5432'
}

db_conn = db.DBconnection(config_path=con_yml_dict, schema='twittervache')
session = db_conn.get_session()
hash_id = db_conn.get_hash_id


class Tweets(db_conn.get_base()):
    __tablename__ = 'vache_tweets'
    def __init__(self, **kwargs):
        if 'hash_id' not in kwargs:
            kwargs['hash_id'] = hash_id(kwargs['id_str'])
            self.id = kwargs['id_str']
        super(Tweets, self).__init__(**kwargs)

    hash_id = Column(String(32), primary_key=True)

    id_str = Column(String)
    tweet_id = Column(BigInteger)
    text = Column(String)
    tweet_created_at = Column(DateTime(timezone=False))
    retweet_count = Column(BigInteger)
    user_id = Column(BigInteger)
    user_screen_name = Column(String)
    user_followers_count = Column(BigInteger)
    user_friends_count = Column(BigInteger)

    dwh_created_at = Column(DateTime(timezone=False), default=db_conn.get_date())
    dwh_updated_at = Column(DateTime(timezone=False), onupdate=db_conn.get_date())


def create_tables():
    db_conn.get_metadata().create_all()

def drop_tables():
    db_conn.get_metadata().drop_all()