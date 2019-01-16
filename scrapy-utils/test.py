# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import requests
from bs4 import BeautifulSoup

#抽屉网爬取
# response = requests.get(
#     url="https://dig.chouti.com/",
#     headers={
#         "user-agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
#     }
# )
# response.encoding = "utf-8"
# soup = BeautifulSoup(response.text, "html.parser")
# content_div = soup.find("div", attrs={"id":"content-list"})
# content_list = content_div.find_all("div", attrs={"class":"item"})
# results = []
# for content_item in content_list:
#     title_div = content_item.find("div", attrs={"class":"part2"})
#     title = title_div.attrs.get("share-title")
#     pic_url = title_div.attrs.get("share-pic")
#     results.append({"title":title, "pic_url":pic_url})
# with open("news.log", mode="a+", encoding="utf-8") as f:
#     for news_item in results:
#         f.write("title:<{0}>,pic_title:<{1}>\n".format(news_item.get("title"), news_item.get("pic_url")))

# 校花 没搞定
# response = requests.get(
#     url="http://www.xiaohuar.com/hua/",
# )
# soup = BeautifulSoup(response.text, "html.parser")
# xiao_hua_s = soup.find_all("div", attrs={"class":"item_t"})
# for index,xiao_hua in enumerate(xiao_hua_s):
#     img_tag = xiao_hua.find("div", attrs={"class":"img"}).find("img")
#     img_url = img_tag.attrs.get("src")
#     print(img_url)
#     res = requests.get("http://www.xiaohuar.com/hua" + img_url)
#     print(res)
#     with open("C:/Users/seven/Desktop/python/utils/scrapy-utils/testscrapy/downloads/{0}.jpg".format(index), "a+", encoding="utf-8") as f:
#         f.write(res.text)


