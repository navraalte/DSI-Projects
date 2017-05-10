# -*- coding: utf-8 -*-
import scrapy
from indeed.items import IndeedItem
from bs4 import BeautifulSoup as bs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IndeedBaseSpider(CrawlSpider):
    name = "indeed_spider2"
    
    start_urls =  ['http://www.indeed.com/q-data-scientist-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-data-analyst-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-data-engineer-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-business-analyst-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-machine-learning-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-software-engineer-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-full-stack-developer-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-front-end-developer-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-back-end-developer-l-San-Francisco,-CA-jobs.html',
                'http://www.indeed.com/q-data-scientist-l-Los-Angeles,-CA-jobs.html',
                'http://www.indeed.com/q-data-analyst-l-Los-Angeles,-CA-jobs.html'
                ]
    
    # Defining rule to crawl next pages
    rules=(Rule(LinkExtractor(restrict_xpaths =['//a[contains(@href,"&pp")]']),follow=True,callback='parse_data'),)

    def parse_start_url(self, response):
        self.parse_data(response)
        
    def parse_data(self, response):
        titles = response.xpath('//h2/a/@title').extract()
        links = response.xpath('//h2/a/@href').extract()
        companies = response.xpath('//span[@class="company"]/span').extract()

        for title, link, comp in zip(titles, links, companies):
            item = IndeedItem()
            item['title'] = title
            abs_url = response.urljoin(link)
            item['url'] = abs_url
            item['company'] = bs(comp).get_text().strip()
            request = scrapy.Request(abs_url, callback=self.parse_job)
            request.meta['item'] = item
            yield request

    def parse_job(self, response):
        item = response.meta['item']
        item['summary'] = response.text
        keys = ['sql', 'python', 'ml', 'spark', 'hadoop', 'dl','numpy','pandas','matplotlib','seaborn','scikit',
        'tensorflow','nosql','d3','mapreduce','aws','linux','matlab','rest','java','time_series','statistics',
        'mongodb','hbase','hive','kafka','cassandra','stata','R','J2EE','git','XML','HTML5','XHTML','JavaScript',
        'jenkins','ruby','scala','RabbitMQ','Redis','C','Cplus','Csharp','angular','node']
        skills = ['SQL', 'Python', 'machine learning',
                  'Spark', 'Hadoop', 'deep learning','Numpy','pandas','matplotlib','seaborn','scikit-learn','tensorflow',
                  'NoSQL','D3','mapreduce','AWS','linux','Matlab','REST','Java','time series','statistic','Mongo','Hbase',
                  'Hive','Kafka','Cassa','Stata','R','J2EE','git','XML','HTML5','XHTML','JavaScript',
                  'jenkins','ruby','scala','RabbitMQ','Redis','C','C++','C#','Angular','node']

        for key, skill in zip(keys, skills):
            item[key] = int(skill in response.text)

        yield item
