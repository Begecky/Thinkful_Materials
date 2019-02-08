import scrapy

class ACSspider(scrapy.Spider):

    name = 'ACS'

    def start_requests(self):
        urls = ['https://api.census.gov/data/2015/acs/acs5?get=NAME,B04004_083E&for=county_subdivision:*&in=state:*&in=county*&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3']
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)
        
    def parse(self, response):
        yield response