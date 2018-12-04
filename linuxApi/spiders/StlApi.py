import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import re
from scrapy.http import Request

class StlApiSpider(scrapy.spiders.Spider):
    name = "StlApiSpider"
    allowed_domains = ["cplusplus.com"]
    start_urls = [
       "http://www.cplusplus.com/reference/"
    ]
    filepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/StlApi.txt'
    logpath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/StlApiLog.txt'
    rooturl = "http://www.cplusplus.com"

    def parse(self, response):

        # print("statt")
        # print(response.body)
        hxs = HtmlXPathSelector(response)
        all_urls = hxs.select('//a/@href').extract()
        # print(all_urls)

        for url in all_urls:
            # print(self.rooturl+url)
            if (url.startswith('/reference')):
                yield Request(self.rooturl+url, callback=self.parse)


        # if re.match('https://www\.kernel\.org/doc/htmldocs/kernel-api/API(-\w+)+\.html', response.url):
        if response.url.startswith('http://www.cplusplus.com/reference'):

            apilist = hxs.select('//section[@id="functions"]/dl[@class="links"]/dt/a/b/text()').extract()

            with open(self.logpath, 'a', encoding='utf-8') as f:
                if (apilist == []):
                    f.write(response.url+'\n')
                else:
                    f.write('!!!'+response.url+'\n')
            # print(apilist)
            # print("stat")
            # print(len(apilist))
            # print("end")
            # funcName = hxs.select('//b[@class="fsfunc"]/text()').extract()
            with open(self.filepath, 'a', encoding='utf-8') as f:
                for i in apilist:
                    f.write(str(i)+" ")


