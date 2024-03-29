import scrapy
import json



class NtschoolsSpider(scrapy.Spider):
    name = 'ntschools'

    start_urls = [
        'https://directory.ntschools.net/#/schools'
    ]

    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': ' BIGipServerdirectory.ntschools.net_443.app~directory.ntschools.net_443_pool=360972810.20480.0000',
        'Host': ' directory.ntschools.net',
        'Pragma': 'no-cache',
        'Referer': 'https://directory.ntschools.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
        'X-Requested-With': 'Fetch'
    }

    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'
        yield scrapy.Request(
            url, callback=self.parse_api, headers=self.headers)

    def parse_api(self, response):
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw_data = response.body
        data = json.loads(raw_data)

        for school in data:
            school_code = school['itSchoolCode']
            school_url = base_url + school_code
            request = scrapy.Request(
                school_url, callback=self.parse_school, headers=self.headers)

            yield request

    def parse_school(self, response):
        raw_data = response.body
        data = json.loads(raw_data)

        yield {
            'Name': data['name'],
            'PhysicalAddress': data['physicalAddress']['displayAddress'],
            'postalAddress': data['postalAddress']['displayAddress'],
            'Email': data['mail'],
            'PhoneNumber': data['telephoneNumber'],
        }
