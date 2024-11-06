import scrapy


class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/ios-phones/"]

    def parse(self, response):
        pass
