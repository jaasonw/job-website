import sys
import time

import schedule
from scrape.scrape_computerjobs import ComputerjobsSpider
from scrape.scrape_linkedin import LinkedinSpider
from scrapy.crawler import CrawlerProcess
from transform import parse


def scrape():
    spider = CrawlerProcess()
    spider.crawl(LinkedinSpider)
    spider.crawl(ComputerjobsSpider)
    spider.start()


def etl():
    scrape()
    parse(upload=True)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        schedule.every(5).hours.do(etl)

        while True:
            schedule.run_pending()
            time.sleep(1)

    if "--scrape-only" in sys.argv:
        scrape()
    elif "--parse-only" in sys.argv:
        if "--upload" in sys.argv:
            parse(upload=True)
        else:
            parse(upload=False)
    elif sys.argv[1] == "--dry-run":
        etl()
