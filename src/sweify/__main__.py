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
    if len(sys.argv) == 1:
        schedule.every().day.at("11:30", "US/Pacific").do(etl)
        schedule.every().day.at("6:00", "US/Pacific").do(etl)

        while True:
            schedule.run_pending()
            time.sleep(1)

    if sys.argv[1] == "--scrape-only":
        scrape()
    elif sys.argv[1] == "--parse-only":
        parse(upload=True)
    elif sys.argv[1] == "--dry-run":
        etl()
