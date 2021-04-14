import scrapy


class QconcursosSpider(scrapy.Spider):
    name = 'qconcursos'

    start_urls = [
        'https://www.qconcursos.com/questoes-de-concursos/questoes'
    ]

    def parse(self, reponse):
        quest = xpath()
        enunciated = xpath()
        answer = xpath()


        yield {

        }
