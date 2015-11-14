#!/usr/bin/env python
# encoding: utf-8


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TouTiaoCategory(Base):
    __tablename__ = 'toutiao_category'

    id = Column(Integer, primary_key=True)
    info = Column(String)
    valid = Column(Integer)
    ctime = Column(Integer)

    def dump2redis(self):
        pass
