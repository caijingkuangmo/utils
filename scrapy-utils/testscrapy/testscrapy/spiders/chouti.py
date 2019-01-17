# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    # def parse(self, response):
    #     print(response,type(response)) # 对象
    #     """
    #     from bs4 import BeautifulSoup
    #     soup = BeautifulSoup(response.text,'html.parser')
    #     content_list = soup.find('div',attrs={'id':'content-list'})
    #     """
    #     # 去子孙中找div并且id=content-list
    #     f = open('news.log', mode='a+')
    #     item_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
    #     for item in item_list:
    #         text = item.xpath('.//a/text()').extract_first()
    #         href = item.xpath('.//a/@href').extract_first()
    #         print(href,text.strip())
    #         f.write(href+'\n')
    #     f.close()
    #
    #     page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
    #     for page in page_list:
    #         from scrapy.http import Request
    #         page = "https://dig.chouti.com" + page
    #         yield Request(url=page,callback=self.parse) # https://dig.chouti.com/all/hot/recent/2

    #response 解析，有xpath，BeautifulSoup， 正则
    # def parse(self, response):

        # 使用bs4 find/find_all
        # from bs4 import BeautifulSoup
        # soup = BeautifulSoup(response.text, "html.parser")
        # content_div = soup.find("div", attrs={"id":"content-list"})
        # content_list = content_div.find_all("div", attrs={"class":"item"})
        # results = []
        # for content_item in content_list:
        #     title_div = content_item.find("div", attrs={"class":"part2"})
        #     title = title_div.attrs.get("share-title")
        #     pic_url = title_div.attrs.get("share-pic")
        #     results.append({"title":title, "pic_url":pic_url})
        # with open("news.log", mode="a+", encoding='utf8') as f:
        #     for news_item in results:
        #         f.write("title:<{0}>,pic_title:<{1}>\n".format(news_item.get("title"), news_item.get("pic_url")))

        # 使用response xpath查找
        # f = open("news.log", mode="a+", encoding="utf8")
        # item_list = response.xpath("//div[@id='content-list']/div[@class='item']")
        # for item in item_list:
        #     text = item.xpath(".//a/text()").extract_first()
        #     href = item.xpath(".//a/@href").extract_first()
        #     f.write("{text}::{href}".format(text=text, href=href))
        # f.close()

    #持久化 items pipelines
    # def parse(self, response):
    #     from testscrapy.items import TestscrapyItem
    #     item_list = response.xpath("//div[@id='content-list']/div[@class='item']")
    #     for item in item_list:
    #         text = item.xpath(".//a/text()").extract_first()
    #         href = item.xpath(".//a/@href").extract_first()
    #         yield TestscrapyItem(title=text, href=href)

    #去重验证
    # def parse(self, response):
    #     print(response.request.url)
    #     page_list = response.xpath("//div[@id='dig_lcpage']//a/@href").extract()
    #     for page in page_list:
    #         from scrapy.http import Request
    #         page = "https://dig.chouti.com{page}".format(page=page)
    #         yield Request(url=page, callback=self.parse)
    #         #配置dont_filter为True后，不去重
    #         # yield Request(url=page, callback=self.parse, dont_filter=True)

    #cookie设置

    # cookie_dict = {}
    # def parse(self, response):
    #
    #     # 携带 解析的方式
    #     #去响应头里获取cookie，cookie保存在cookie_jar对象
    #     from scrapy.http.cookies import CookieJar
    #     from urllib.parse import urlencode
    #     cookie_jar = CookieJar()
    #     cookie_jar.extract_cookies(response, response.request)
    #     # 去对象中将cookie解析到字典
    #     for k, v in cookie_jar._cookies.items():
    #         for i, j in v.items():
    #             for m, n in j.items():
    #                 self.cookie_dict[m] = n.value
    #
    #     yield Request(
    #         url="https://dig.chouti.com/login",
    #         method="POST",
    #         #body 可以自定拼接，也可以使用urlencode拼接
    #         body="phone=8613121758648&password=woshiniba&oneMonth=1",
    #         cookies=self.cookie_dict,
    #         headers={
    #             "Content-Type":'application/x-www-form-urlencoded; charset=UTF-8'
    #         },
    #         callback=self.check_login
    #     )
    #
    # def check_login(self, response):
    #     print(response.text)
    #     yield Request(
    #         url="https://dig.chouti.com/all/hot/recent/1",
    #         cookies=self.cookie_dict,
    #         callback=self.index
    #     )
    #
    # def index(self, response):
    #     news_list = response.xpath("//div[@id='content-list']/div[@class='item']")
    #     for new in news_list:
    #         link_id = new.xpath(".//div[@class='part2']/@share-linkid").extract_first()
    #         yield Request(
    #             url="http://dig.chouti.com/link/vote?linksId=%s"%(link_id, ),
    #             method="POST",
    #             cookies=self.cookie_dict,
    #             callback=self.check_result
    #         )
    #
    #     page_list = response.xpath("//div[@id='dig_lcpage']//a/@href").extract()
    #     for page in page_list:
    #         page = "https://dig.chouti.com" + page
    #         yield Request(url=page, callback=self.index)
    #
    # def check_result(self, response):
    #     print(response.text)

    #start_urls
    # def start_requests(self):
    #     '''在这里你可以定义获取url的地方，比如从redis中获取'''
    #     #方式一 生成器
    #     # for url in self.start_urls:
    #     #     yield Request(url=url)
    #
    #     #方式二 返回一个列表
    #     req_list = []
    #     for url in self.start_urls:
    #         req_list.append(Request(url=url))
    #     return req_list
    #
    # def parse(self, response):
    #     print

    def parse(self, response):
        print(type(response.text))


