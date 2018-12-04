import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import re
from scrapy.http import Request


class WinApiSpider(scrapy.spiders.Spider):
    name = "WinApiSpider"
    allowed_domains = ["microsoft.com"]
    start_urls = [
        "https://docs.microsoft.com/zh-cn/previous-versions/windows/dn424765(v=win.10)"
    ]
    filepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/WinApi.txt'

    def parse(self, response):

        # print("statt")
        # print(response.body)
        hxs = HtmlXPathSelector(response)
        # all_urls = hxs.select('//a/@href').extract()
        # print(all_urls)
        # for url in all_urls:
        #     yield Request(self.start_urls[0] + url, callback=self.parse)

        # if re.match('https://www\.kernel\.org/doc/htmldocs/kernel-api/API(-\w+)+\.html', response.url):
        # if response.url.startswith('https://www.kernel.org/doc/htmldocs/kernel-api/API-'):
        #     funcName = hxs.select('//b[@class="fsfunc"]/text()').extract()
        #     with open(self.filepath, 'a', encoding='utf-8') as f:
        #         f.write(str(funcName[0]) + " ")
        funcName = hxs.select('//li/a/strong/text()').extract()
        # print(len(funcName))
        with open(self.filepath, 'a', encoding='utf-8') as f:
            for i in funcName:

                f.write(str(i) + " ")