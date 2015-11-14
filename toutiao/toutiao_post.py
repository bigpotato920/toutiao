from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TouTiaoPost(Base):
    __tablename__ = 'toutiao_post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    summary = Column(String)
    date = Column(String)
    ctime = Column(Integer)
    utime = Column(Integer)
