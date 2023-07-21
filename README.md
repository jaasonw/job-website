# sweify

automatically scrape, parse, and curate jobs for new grads and interns.

designed to pick up on the work done by [FreshSWE](https://www.freshswe.com/)

# how it works

1. a cron job runs the scraper every n interval then parses and stores the data into google sheets
2. a next.js frontend using isr fetches the google sheet and displays it on a website
