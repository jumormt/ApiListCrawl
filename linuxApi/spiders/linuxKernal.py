import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import re
from scrapy.http import Request

class LinuxKernalApiSpider(scrapy.spiders.Spider):
    name = "linuxApiSpider"
    allowed_domains = ["kernel.org"]
    start_urls = [
        "https://www.kernel.org/doc/htmldocs/kernel-api/"
    ]
    filepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/linuxApi2.txt'

    def start_requests(self):
        urls = [
            'https://www.kernel.org/doc/htmldocs/kernel-api/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # print("statt")
        # print(response.body)
        hxs = HtmlXPathSelector(response)
        all_urls = hxs.select('//a/@href').extract()
        # print(all_urls)
        for url in all_urls:
            yield response.follow(url, self.parse)


        # if re.match('https://www\.kernel\.org/doc/htmldocs/kernel-api/API(-\w+)+\.html', response.url):
        if response.url.startswith('https://www.kernel.org/doc/htmldocs/kernel-api/API-'):
            funcName = hxs.select('//b[@class="fsfunc"]/text()').extract()
            with open(self.filepath, 'a', encoding='utf-8') as f:
                f.write(str(funcName[0])+" ")


