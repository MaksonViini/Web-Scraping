import scrapy


class QconcursosSpider(scrapy.Spider):
    name = 'qconcursos'
    
    start_urls = [
        'https://www.qconcursos.com/questoes-de-concursos/questoes'
    ]
