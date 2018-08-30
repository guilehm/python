import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.uol.com.br']

    def parse(self, response):
        self.log('Visitei o site: {}'.format(response.url))
