from scrape.scrape_linkedin import scrape
from transform import parse

if __name__ == "__main__":
    scrape()
    parse(upload=True)
