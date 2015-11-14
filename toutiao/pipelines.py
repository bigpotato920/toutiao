# -*- coding: utf-8 -*-
import hashlib
import json
import time
from scrapy.exceptions import DropItem
from .db_config import redis
from .db_config import DBSession
from .toutiao_post import TouTiaoPost
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DuplicatesPipeline(object):
    def __init__(self):
        self.expire_time = 24 * 60 * 60

    def process_item(self, item, spider):
        item_json = json.dumps(item.values(), sort_keys=True)
        item_md5 = hashlib.md5(item_json).hexdigest()
        if redis.exists(item_md5):
            raise DropItem("Duplicate item found: %s" % self.debug_item(item))
        else:
            redis.setex(item_md5, self.expire_time, item_json)
        return item

    def debug_item(self, item):
        return '时间：%s，标题：%s，url：%s，总结：%s' \
            % (item['date'], item['title'], item['url'], item['summary'])


class DatabasePipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        current_time = int(time.time())
        post = TouTiaoPost(title=item["title"], url=item["url"],
            summary=item["summary"], date=item["date"], ctime=current_time, utime=current_time)
        self.session.add(post)
        self.session.commit()

    def close_spider(self, spider):
        self.session.close()
