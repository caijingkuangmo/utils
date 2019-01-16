# -*- coding: utf-8 -*-
import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    # def parse(self, response):
    #
    #     # 使用bs4 find/find_all
    #     from bs4 import BeautifulSoup
    #     soup = BeautifulSoup(response.text, "html.parser")
    #     content_list = soup.find("div", attrs={"id":"content-list"})
    #     results = []
    #     for content_item in content_list:
    #         title_div = content_item.find("div", attrs={"class":"part2"})
    #         title = title_div.attrs.get("share-title")
    #         pic_url = title_div.attrs.get("share-pic")
    #         results.append({"title":title, "pic_url":pic_url})
    #     with open("news.log", mode="a+") as f:
    #         for news_item in results:
    #             f.write("title:<{0}>,pic_title:<{1}>\n".format(news_item.get("title"), news_item.get("pic_url")))
    #
    #     # 使用response xpath查找
    #

    def parse(self, response):
        # print(response,type(response)) # 对象
        # print(response.text)
        """
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text,'html.parser')
        content_list = soup.find('div',attrs={'id':'content-list'})
        """
        # 去子孙中找div并且id=content-list
        f = open('news.log', mode='a+')
        item_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
        for item in item_list:
            text = item.xpath('.//a/text()').extract_first()
            href = item.xpath('.//a/@href').extract_first()
            print(href,text.strip())
            f.write(href+'\n')
        f.close()

        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            from scrapy.http import Request
            page = "https://dig.chouti.com" + page
            yield Request(url=page,callback=self.parse) # https://dig.chouti.com/all/hot/recent/2