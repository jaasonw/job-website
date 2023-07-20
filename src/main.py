import schedule
import time
from scrape import scrape_linkedin
from transform import parse


def etl():
    scrape_linkedin.scrape()
    parse(upload=True)


if __name__ == "__main__":
    schedule.every().day.at("10:00").do(etl)
    schedule.every().day.at("22:00").do(etl)

    while True:
        schedule.run_pending()
        time.sleep(1)
