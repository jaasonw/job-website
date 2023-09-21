import csv
import urllib.parse
from urllib.parse import urljoin, urlparse

import scrapy
from scrapy.crawler import CrawlerProcess


class ComputerjobsSpider(scrapy.Spider):
    name = "computerjobs"

    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 5,
        "AUTOTHROTTLE_MAX_DELAY": 60,
        "DOWNLOAD_DELAY": 3,
    }

    def start_requests(self):
        with open(self.name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["URL", "Title", "Company", "Date", "Description", "Location", "Source"]
            )

        urls = ["https://www.computerjobs.com/us/en/JobListing.aspx?shid=97A7F115B70CEA379778"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_job_list)

    def parse_job_list(self, response):
        print(response)


def scrape():
    process = CrawlerProcess()
    process.crawl(ComputerjobsSpider)
    process.start()

scrape()