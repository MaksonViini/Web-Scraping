import scrapy
from ..items import ScrapytutorialItem

class MercadoLivre(scrapy.Spider):
    name = 'mercadolivre'

    start_urls = [
        'https://www.mercadolivre.com.br/'
    ]

    def parse(self, response):
        for i in response.xpath('//li[@class="promotion-item"]'):
            