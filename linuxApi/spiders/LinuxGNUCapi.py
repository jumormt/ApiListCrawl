import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import re
from scrapy.http import Request

class LinuxGNUApiSpider(scrapy.spiders.Spider):
    name = "linuxGNUApiSpider"
    allowed_domains = ["gnu.org"]
    start_urls = [
        "http://www.gnu.org/software/libc/manual/html_node/Function-Index.html"
    ]
    filepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/GNUApi.txt'


    def parse(self, response):

        # print("statt")
        # print(response.body)
        hxs = HtmlXPathSelector(response)
        # all_urls = hxs.select('//a/@href').extract()
        # # print(all_urls)
        # for url in all_urls:
        #     yield Request(self.start_urls[0]+url, callback=self.parse)
        result = hxs.select('//tr/td[2]/a/code/text()').extract()
        # print(result)
        with open(self.filepath, 'a', encoding='utf-8') as f:
            for i in result:
                if i:
                    f.write(i + " ")


        # if re.match('https://www\.kernel\.org/doc/htmldocs/kernel-api/API(-\w+)+\.html', response.url):
        # if response.url.startswith('https://www.kernel.org/doc/htmldocs/kernel-api/API-'):
        #     funcName = hxs.select('//b[@class="fsfunc"]/text()').extract()
        #     with open(self.filepath, 'a', encoding='utf-8') as f:
        #         f.write(str(funcName[0])+" ")


