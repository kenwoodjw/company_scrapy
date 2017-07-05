# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql #导入数据库
from company_scrapy import settings#导入配置
# from scrapy import log
from company_scrapy.items import CompanyScrapyItem
import  six


class CompanyScrapyPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            port =settings.MYSQL_PORT,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__==CompanyScrapyItem:
            try:
                # print (type(item['company'][0]))
                sql = "insert INTO %s (%s) VALUES ('%s')"%('company_name','company',item['company'][0])
                # print (sql)
                self.cursor.execute(sql)
                self.connect.commit()
            except Exception as error:
                print (error)
            return item
