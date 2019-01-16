# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 下面这种方式 还没有解决反复打开链接的问题，就是每次item都会打开链接和关闭连接

# class FilePipeline(object):
#     def process_item(self, item, spider):
#         with open("news.log", "a+", encoding="utf8") as f:
#             f.write("{title}::{href}\n".format(title=item.get("title").strip(), href=item.get("href")))
#         return item
#
# class MongodbPipeline(object):
#     def process_item(self, item, spider):
#         import pymongo
#         mongo_conn = pymongo.MongoClient("localhost", 27017)
#         db = mongo_conn["test"]
#         coll = db["chouti"]
#         coll.insert_one({
#             "title":item.get("title"),
#             "href":item.get("href")
#         })
#         return item

# 解决反复连接问题
'''
1. 判断当前FilePipeline类中是否有from_crawler
    有：
        obj = FilePipeline.from_crawler(....)
    否：
        obj = FilePipeline()

    所以你可以在这个from_crawler类方法获取文件存储路径，以及存储配置什么

2.执行open_spider方法，在这里你可以打开链接

3.反复执行process_item

4.执行close_spider方法，在这里你可以关闭连接
'''

class FilePipeline(object):
    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):
        print("FilePipeline.from_crawler")
        path = crawler.settings.get("HREF_FILE_PATH")
        return cls(path)

    def open_spider(self, spider):
        print("FilePipeline.open_spider")
        self.f = open(self.path, "a+", encoding="utf8")

    def process_item(self, item, spider):
        print("FilePipeline.process_item")
        self.f.write("{title}::{href}\n".format(title=item.get("title").strip(), href=item.get("href")))

    def close_spider(self, spider):
        print("FilePipeline.close_spider")
        self.f.close()
