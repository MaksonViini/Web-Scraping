from urllib import parse
import scrapy


class NbaSpider(scrapy.Spider):
    name = 'nba'

    start_urls = [
        'https://www.nba.com/players'
    ]

    def parse(self, response):
        for x, i in enumerate(response.xpath('.//tr')):
            player_first_name = response.xpath(
                './/div[@class="flex flex-col lg:flex-row"]/p[1]//text()')[x].get()

            player_last_name = response.xpath(
                './/div[@class="flex flex-col lg:flex-row"]/p[2]//text()')[x].get()

            team = response.xpath('.//a[@class="t6"]//text()')[x].get()

            number = response.xpath('.//td[3]//text()')[x].get()

            position = response.xpath('.//td[@class="text"]//text()')[1].get()

            heigth = response.xpath('.//td[5]//text()')[x].get()

            weigth = response.xpath('.//td[6]//text()')[x].get()

            last_attended = response.xpath('.//td[7]//text()')[x].get()

            country = response.xpath('.//td[8]//text()')[x].get()

            yield {
                'player': player_first_name + ' ' + player_last_name,
                'team': team,
                'number': number,
                'position': position,
                'heigth': heigth,
                'weigth': weigth,
                'last_attended': last_attended,
                'country': country
            }
