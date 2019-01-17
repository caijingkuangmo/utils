# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TestscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        print("process_spider_input")
        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        print("process_spider_output")
        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
        print("只在爬虫启动时，执行一次")
        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TestscrapyDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        print("download middlewares process_request")
        #1.返回response对象,这种情况下不执行下载，但是还是会执行process_response
        # from scrapy.http import HtmlResponse
        # import requests
        # result = requests.get(request.url)
        # return HtmlResponse(
        #     url=request.url,
        #     status=200,
        #     headers=None,
        #     body=result.content
        # )

        # 2.发起下次请求
        # from scrapy.http import Request
        # print('request')
        # return Request("https://dig.chouti.com/r/tec/hot/1")

        # 3.抛出异常,不执行process_response，会执行process_exception
        # from scrapy.exceptions import IgnoreRequest
        # raise IgnoreRequest

        # 4. 对请求进行加工(*)
        # request.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        return None

    def process_response(self, request, response, spider):
        print("download middlewares process_response")
        return response

    def process_exception(self, request, exception, spider):
        print("download middlewares process_exception")
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
