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
        job_list = [
            urljoin(url, urlparse(url).path) 
                for url in response.xpath("/html/body/form//div[@class='jobListItem newjobsum']/div[1]/a[@class='jobListPosition']")
                    .xpath("@href").getall()
        ]
        self.log(job_list)
        yield from response.follow_all(job_list, self.parse_job)
        
    def parse_job(self, response):
        self.log(response.url)
        description = (
            " ".join(response.xpath("//*[@id='md_skills']")
                .css("*::text")
                .extract())
        )
        date_posted = (
            response.xpath("//*[@id='md_posted_date']/text()").get().strip()
        )
        location = (
            response.xpath("//*[@id='md_location']/text()").get().strip()
        )

        contact = response.xpath("//*[@id='md_recruiter']/a/span/span/text()").get()
        if not contact:
            contact = response.xpath("//*[@id='td_posted_by']/text()").get()

        result = {
            "url": response.url,
            "title": response.xpath("//*[@id='td_jobpositionnolink']/text()").get().strip(),
            "company": contact,
            "date_posted": date_posted,
            "description": description,
            "location": location,
            "source": self.name,
        }

        with open(self.name + ".csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(list(result.values()))
