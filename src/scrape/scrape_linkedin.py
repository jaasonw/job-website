import csv
import re
import statistics
import urllib.parse
from urllib.parse import urljoin, urlparse

import pygsheets
import scrapy
from scrapy.crawler import CrawlerProcess


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"

    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 5,
        "AUTOTHROTTLE_MAX_DELAY": 60,
        "DOWNLOAD_DELAY": 3,
    }

    def start_requests(self):
        params = {
            "keywords": "Software Engineer",
            "location": "California, United States",
            "geoId": "102095887",
            "trk": "public_jobs_jobs-search-bar_search-submit",
            "f_TPR": "r2592000",
            "position": 1,
            "pageNum": 0,
            "start": 0,
        }
        urls = []
        for i in range(3):
            params["pageNum"] = i
            params["start"] = i * 25
            urls.append(
                f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?{urllib.parse.urlencode(params)}"
            )
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_job_list)

    def parse_job_list(self, response):
        job_list = [
            urljoin(url, urlparse(url).path)
            for url in response.xpath("/html/body/li/div/a").xpath("@href").getall()
        ]
        self.log(job_list)
        yield from response.follow_all(job_list, self.parse_job)

    def parse_job(self, response):
        self.log(response.url)
        self.log(
            response.xpath(
                "/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1/text()"
            )
            .get()
            .strip()
        )
        description = " ".join(
            response.xpath(
                "/html/body/main/section[1]/div/div/section[1]/div/div/section/div"
            )
            .css("*::text")
            .extract()
        )
        date_posted = (
            response.xpath(
                "/html/body/main/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/span/text()"
            )
            .get()
            .strip()
        )
        location = (
            response.xpath(
                "/html/body/main/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]/text()"
            )
            .get()
            .strip()
        )
        result = {
            "url": response.url,
            "title": response.xpath(
                "/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1/text()"
            )
            .get()
            .strip(),
            "company": response.xpath(
                "/html/body/main/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]/a/text()"
            )
            .get()
            .strip(),
            "date_posted": date_posted,
            "description": description,
            "location": location,
            # "years_of_experience": years_of_experience,
        }
        # sh.sheet1.append_table(
        #     list(result.values()), start="A1", end=None, dimension="ROWS"
        # )
        with open("linkedin.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(list(result.values()))
            # writer.writerows(list(result.values()))
            # f.write(",".join() + "\n")
        # self.log(list(result.values()))
        yield result["url"]


def scrape():
    process = CrawlerProcess()
    process.crawl(LinkedinSpider)
    process.start()


if __name__ == "__main__":
    scrape()
