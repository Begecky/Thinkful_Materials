import scrapy
from scrapy.crawler import CrawlerProcess

class ACSspider(scrapy.Spider):
			name = 'ACS'
			
			def start_requests(self):
						 urls = ['https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:01&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:02&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:03&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:04&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:05&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:06&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:07&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:08&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:09&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												'https://api.census.gov/data/2017/acs/acs1?getNAME=B04004_083E&for=county:*&in=state:10&key=db912d46f4c0fc8b306cc0ffe95dfbe707d9f1a3',
												]
						 for url in urls:
										yield scrapy.Request(url = url, callback = self.parse)
																
			def parse(self, response):
							jsonresponse = json.loads(response.text)
						        
							item = MyItem()
							item['PopCount'] = jsonresponse["B04004_083E"]
							item['Name'] = jsonresponse['NAME']
							item['State'] = jsonresponse['state']
							item['County'] = jsonresponse['county']
						        
							return item
										
						