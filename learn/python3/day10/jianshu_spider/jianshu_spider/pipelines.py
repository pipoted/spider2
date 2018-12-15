# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from twisted.enterprise import adbapi
from pymysql import cursors


# class JianshuSpiderPipeline(object):
#
#     def __init__(self) -> None:
#         self.conn = pymysql.connect(
#             host='localhost',
#             user='root',
#             password='xzx199110',
#             database='spider',
#             port=3306,
#             charset='utf8'
#         )
#         self.cursor = self.conn.cursor()
#         self._sql = None
#
#     def process_item(self, item, spider):
#         self.cursor.execute(self.sql,
#                             (item['title'], item['content'], item['article_id'], item['author'], item['avatar'],
#                              item['origin_url'], item['pub_time']))
#         self.conn.commit()
#         return item
#
#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql = """
#             insert into article(id, title, content, article_id, author, avatar, origin_url, pub_time) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)
#             """
#             return self._sql
#
#         return self._sql


class JianshuTwistedPipeline(object):

    def __init__(self) -> None:
        db_params = {
            'host': 'localhost',
            'user': 'root',
            'password': 'xzx199110',
            'database': 'spider',
            'port': 3306,
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor,
        }

        self.db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id, title, content, article_id, author, avatar, origin_url, pub_time, read_count, like_count, word_count, subjects, comment_count) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            return self._sql

        return self._sql

    def process_item(self, item, spider):
        defer = self.db_pool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['title'], item['content'], item['article_id'], item['author'], item['avatar'],
                                  item['origin_url'], item['pub_time'], item['read_count'], item['like_count'],
                                  item['word_count'], item['subjects'], item['comment_count']))

    def handle_error(self, error, item, spider):
        print('-' * 30 + 'error' + '-' * 30)
        print(error)
        print('-' * 30 + 'error' + '-' * 30)
