import scrapy
from quotes.items import SportsquotesItem
from bs4 import BeautifulSoup as bs


class SportBaseSpider(scrapy.Spider):
	name = "quotecrawler"
	start_urls = ['http://ftw.usatoday.com/2015/04/best-101-sports-facts-trivia-crazy-amazing-incredible-babe-ruth-michael-phelps-michael-jordan']

	def parse(self,response):
		#/'//span[@class="company"]/span'
		#//h2/a/@title'
		quotes = response.xpath("//div[@class='entry-content ']/div[@class='articleBody']/h4/text()").extract()


		for quote in zip(quotes):
			item = SportsquotesItem()
			item['quote'] = quote

			yield item
