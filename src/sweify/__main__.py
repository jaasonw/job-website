import sys
import time

import schedule
from scrape import scrape_linkedin
from scrape.scrape_linkedin import scrape
from transform import parse


def etl():
    scrape_linkedin.scrape()
    parse(upload=True)


if __name__ == "__main__":
    if sys.argv[1] == "--scrape-only":
        scrape()
    elif sys.argv[1] == "--parse-only":
        parse(upload=True)
    elif sys.argv[1] == "--dry-run":
        etl()
    else:
        schedule.every().day.at("10:00").do(etl)
        schedule.every().day.at("22:00").do(etl)

        while True:
            schedule.run_pending()
            time.sleep(1)
