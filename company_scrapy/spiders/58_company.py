# #coding:utf-8
import  scrapy
from scrapy.selector import Selector #导入选择器
from company_scrapy.items import  CompanyScrapyItem #引用
from scrapy.http import  request
from company_scrapy.spiders import get_url
class Scrapy(scrapy.Spider):
    name='58'
    allow_domain=['http://qy.58.com']
    start_urls=get_url.get_url()

    def parse(self,response):
        items=[]
        for sel in response.xpath('//ul/li/span'):
            item=CompanyScrapyItem()
            item['company']=sel.xpath('a/text()').extract()
            items.append(item)

        return items


