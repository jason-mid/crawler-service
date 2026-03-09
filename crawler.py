import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://example.com']

    def parse(self, response):
        title = response.css('title::text').get()
        yield {'title': title}

# To run this spider, use the command: scrapy crawl myspider
