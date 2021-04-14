import scrapy


class QconcursosSpider(scrapy.Spider):
    name = 'qconcursos'

    start_urls = [
        'https://www.qconcursos.com/questoes-de-concursos/questoes'
    ]

    def parse(self, response):
        for i in response.xpath('//div[@class="q-questions-list js-questions-list"]'):
            id_quest = i.xpath('//span[@class="q-index js-question-index visible"]//text()')
            enunciated = i.xpath(
                '//div[@class="q-question-enunciation"]/span//text()').get()
            questions = i.xpath()
            answer = i.xpath()

        yield {
            'id_quest': id_quest,
            'enunciated': enunciated,
            'questions': questions,
            'answer': answer
        }
