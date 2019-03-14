# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class NewsfetchPipeline(object):
    def open_spider(self, spider):
        hostname = 'piro.ceubekalawiz.us-east-2.rds.amazonaws.com' #host
        username = 'piro' #username
        password = 'research123' # your password
        database = 'piro' #database name
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if spider.name == 'republic':
            self.cur.execute("insert into feed_republic(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item


        if spider.name == 'ndtv':
            self.cur.execute("insert into feed_ndtv(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item

        if spider.name == 'indiatv':
            self.cur.execute("insert into feed_indiatoday(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item

        if spider.name == 'thehindu':
            self.cur.execute("insert into feed_thehindu(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item

        if spider.name == 'zee':
            self.cur.execute("insert into feed_zeenews(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item

        if spider.name == 'hindustan':
            self.cur.execute("insert into feed_hindustan(headline,link) values(%s,%s)",(item['headline'],item['link']))
            self.connection.commit()
            return item
