import scrapy
import json
import codecs
import datetime

def writeTofile(fileName, text):
    with codecs.open(fileName, 'w', 'utf-8') as outfile:
        outfile.write(text)
class MediumScraper(scrapy.Spider):
    name = 'medium_scraper'
    handle_httpstatus_list = [401, 400]
    autothrottle_enabled = True
    def start_requests(self):
        start_urls = ['https://medium.com/search?q=Artificial%20Intelligence%20%20%20Literature']
        for url in start_urls:
            yield scrapy.Request(url, method = 'POST', callback = self.parse)
    def parse(self, response):
        results = response.text
        split_results = results.split("while(1);</x>")
        results = split_results[1]
        filename = 'AI_Literature.json'
        writeTofile(filename, results)
        with codecs.open(results, 'r', 'utf-8') as infile:
            data = json.load(infile)
        if 'paging' in data['payload']:
            data = data['payload']['paging']
            if 'next' in data:
                print('Hold on, bra - gettin the next page.')
                data = data['next']
                formdata = {'ignoreIds' : data['ignoreIds'],
                                        'page' : data['page'],
                                        'pageSize' : data['pageSize']}
                header = 'Request Payload'
                yield scrapy.Request('https://medium.com/search?q=Artificial%20Intelligence%20%20%20Literature', method = 'POST', body = json.dumps(formdata), headers = header, callback = self.parse)
        