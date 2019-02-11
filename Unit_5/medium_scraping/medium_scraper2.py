import scrapy
import json
import codecs

class MediumScraper(scrapy.Spider):
    name = 'medium_scraper'
    handle_httpstatus_list = [401, 400]
    autothrottle_enabled = True
    
    start_urls = ['https://medium.com/search?q=Artificial%20Intelligence%20%20%20Literature']
    
    def parse(self, response):
        for article_url in response.xpath('.//*[@id="_obv.shell._surface_1549759765777"]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]').extract():
            yield response.follow(article_url, callback = self.parse_article)
        next_results = response.css('./ ::next').extract_first()
        if next_results is not None:
            yield response.follow(next_results, callback = self.parse)
            
    def parse_article(self, response):
        content = response.xpath('.//*[@id="_obv.shell._surface_1549759765777"]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/a').extract()
        yield {'article' : ''.join(content)}
        
        