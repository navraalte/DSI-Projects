# -*- coding: utf-8 -*-

import scrapy
from webscraper.items import  WebscraperItem



class IndeedSpider(scrapy.Spider):


    name = "indeed_spider"
    allowed_domains = ["indeed.com"]


    # job query key terms 
    job_sites = ["https://www.indeed.com/jobs"]
    job_titles = ["Data Scientist", 'Machine Learning Engineer', "Data Analyst"]
    # citites_stats = \
    # [("New York", 'NY'), ("Los Angeles", "CA"), ("San Diego", 'CA'), ('Chicago', 'IL'), 
    #  ("Dallas", "TX"), ("Houston", "TX"), ("Washington", 'DC'), ("Philadelphia", "PA"), 
    # ("Miami", "FL"), ("Atlanta", "GA"), ("Boston", "MA"), ("San Francisco", "CA"), 
    # ("Phoenix", "AZ"), ("San Bernardino", "CA"), ("Detroit", "MI"), ("Seattle", "WA"), 
    # ("Minneapolis", "MN"), ("Tampa", "FL"), ("Denver", "CA"), ("St. Louis", "IL"), 
    # ("Las Vegas", "NV")]

    citites_stats = \
    [("New York", 'NY'), ("Los Angeles", "CA"), ("San Diego", 'CA')]


    # increment page in order to scrap additonal posting in same city
    page_increment_list = ['0','1','2','3','4']

    # list populated with unique combinations of job query key terms
    #these combinations form unique urls to scrap 
    # start_urls = (
    #     'https://www.indeed.com/jobs?q=Data+Scientist&l=San+Bernardino%2C+CA&start=2',
    # )


    url_list = []
    for site in job_sites:
        for  title in job_titles:
            for city, state in citites_stats:
                for page in page_increment_list:

                    title = "+".join(title.split(" "))
                    city = "+".join(city.split(" "))
                    url = site + "?q=" + title + "&l=" + city + "%2C+" + state
                    # incremental_page values increment by 10
                    if page != None:
                        url = url + "&start=" +   page
                    url_list.append(url)

    start_urls = url_list





    def parse(self, response):
        titles = response.xpath('//h2/a/@title').extract()
        links = response.xpath('//h2/a/@href').extract()
        companies = response.xpath('//span[@class="company"]/span/text()').extract()

        for title, link, comp in zip(titles, links, companies):
            item = WebscraperItem()
            item['title'] = title
            abs_url = response.urljoin(link)
            item['url'] = abs_url
            item['company'] = comp

            request = scrapy.Request(abs_url, callback=self.parse_job)
            request.meta['item'] = item
            yield request


    def parse_job(self, response):
        item = response.meta['item']
        keys = ['sql', 'python', 'ml', 'spark', 'hadoop', 'dl',
                'stats', 'ts', 'de', 'dp', 
                'nlp', 'bd', 'pca', 'pred_modeling', 
                'anomaly_detection', 'data_analysis', 
                'exp_design', 'cnn', 'bayes_opt', 'pipeline']

        skills = ['sql', 'python', 'machine learning',
                  'spark', 'hadoop', 'deep learning', 
                  'statistics', 'time series', 'data engineering', 
                  'data products', 'nlp', 'big data', 
                  'pca', 'predictive modeling', 'anomaly detection', 
                  'data analysis', 'experimental design', 
                  'deep convolutional networks','bayesian optimization',
                  'pipeline']

        for key, skill in zip(keys, skills):
            item[key] = int(skill in response.text.lower())

        yield item


# ToDo 
# pipe data to S3 bucket
# create url template for custom job searches
# scrape salaries 
# use pipelines.py to pipe data to sql db on S3

    