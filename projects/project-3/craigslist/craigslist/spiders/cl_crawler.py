import scrapy
from craigslist.items import CraigslistItem
from bs4 import BeautifulSoup as bs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CraigsListSpider(CrawlSpider):
	name = "craigslistCrawl"

	start_urls = ['https://lasvegas.craigslist.org/search/rva',
				 'http://miami.craigslist.org/search/rva',
				 'http://saltlakecity.craigslist.org/search/rva',
				 'http://anchorage.craigslist.org/search/rva',
				 'http://cleveland.craigslist.org/search/rva',
				 'http://baltimore.craigslist.org/search/rva',
				 'http://houston.craigslist.org/search/rva',
				 'http://newyork.craigslist.org/search/rva',
				 'http://phoenix.craigslist.org/search/rva',
				 'http://denver.craigslist.org/search/rva',
				 'http://detroit.craigslist.org/search/rva',
				 'http://seattle.craigslist.org/search/rva',
				 'http://portland.craigslist.org/search/rva',
				 'http://sfbay.craigslist.org/search/rva',
				 'http://boston.craigslist.org/search/rva',
				 'http://miami.craigslist.org/search/rva',
				 'http://saltlakecity.craigslist.org/search/rva',
				 'http://anchorage.craigslist.org/search/rva',
				 'http://cleveland.craigslist.org/search/rva',
				 'http://baltimore.craigslist.org/search/rva',
				 'http://houston.craigslist.org/search/rva',
				 'http://newyork.craigslist.org/search/rva',
				 'http://phoenix.craigslist.org/search/rva',
				 'http://denver.craigslist.org/search/rva',
				 'http://detroit.craigslist.org/search/rva',
				 'http://seattle.craigslist.org/search/rva',
				 'http://portland.craigslist.org/search/rva',
				 'http://sfbay.craigslist.org/search/rva',
				 'http://boston.craigslist.org/search/rva']

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//a[@title="next page"]']),follow=True,callback='parse_data'),)

	def parse_data(self,response):
		#/'//span[@class="company"]/span'
		#//h2/a/@title'
		prices = response.xpath("//span[@class='result-meta']/span[@class='result-price']/text()").extract()
		details = response.xpath("//a[@class='result-title hdrlnk']/text()").extract()
		areas = response.xpath("//select[@id='areaAbb']/option/text()").extract()


		for price, detail, area in zip(prices, details, areas):
			item = CraigslistItem()
			item['price'] = price
			item['detail'] = detail
			item['area'] = area

			yield item
