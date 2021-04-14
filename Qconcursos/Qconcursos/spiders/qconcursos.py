import scrapy


class QconcursosSpider(scrapy.Spider):
    name = 'qconcursos'

    start_urls = [
        'https://www.qconcursos.com/questoes-de-concursos/questoes'
    ]

    

    def parse(self, response):
        x = 1
        # for i in response.xpath('//div[@class="js-question-item q-question-item"]'):
            # id_quest = i.xpath(
            #     '//span[@class="q-index js-question-index visible"]//text()').get()

        id_quest = x

        enunciated = response.xpath(
            '//div[@class="q-question-enunciation"]//text()').get()

        # questions = i.xpath()

        # answer = i.xpath()
        x += 1

        yield {
            'id_quest': id_quest,
            'enunciated': enunciated,
            # 'questions': questions,
            # 'answer': answer
        }
