from urllib import parse
import scrapy


class NbaSpider(scrapy.Spider):
    name = 'nba'

    start_urls = [
        'https://www.nba.com/players'
    ]


    # .//select[contains(@title, "Page Number Selection Drown Down List")]/option[1] Xpath para o all
    # response.xpath('.//select[contains(@title, "Page Number Selection Drown Down List")]/option[1]').get()
    
    def parse(self, response):
        
        for i in response.xpath('.//tbody//tr'):

            player_first_name = str(i.xpath(
                './/div[@class="flex flex-col lg:flex-row"]/p[1]//text()').get())

            player_last_name = str(i.xpath(
                './/div[@class="flex flex-col lg:flex-row"]/p[2]//text()').get())

            team = i.xpath('.//a[@class="t6"]//text()').get()

            number = i.xpath('.//td[3]//text()').get()

            position = i.xpath('.//td[4]//text()').get()

            heigth = i.xpath('.//td[5]//text()').get()

            weigth = i.xpath('.//td[6]//text()').get()

            last_attended = i.xpath('.//td[7]//text()').get()

            country = i.xpath('.//td[8]//text()').get()

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

            # next_page = response.xpath(
            #     '//button[contains(@title,"Next Page Button")]').get()

            # if next_page:
            #     yield scrapy.Request(url=next_page, callback=self.parse)
