import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


redis = redis.StrictRedis(host='localhost', port=6379, db=0)
engine = create_engine('mysql://root:root@localhost/toutiao_crawler?charset=utf8',
        encoding="utf8", echo=True)
DBSession = sessionmaker(bind=engine)
