from scrapy.crawler import CrawlerProcess
from scrape.scrape_linkedin import LinkedinSpider


def main():
    process = CrawlerProcess()
    process.crawl(LinkedinSpider)
    process.start()


if __name__ == "__main__":
    main()
