import scrapy

class ACSspider(scrapy.Spider):
			name = 'ACS'
			
			def start_requests(self):
						urls = ['https://api.census.gov/data/2017/acs/acs1?get=B04004_083E,NAME&for=county:*&in=state:06'
												]
						for url in urls:
										yield scrapy.Request()