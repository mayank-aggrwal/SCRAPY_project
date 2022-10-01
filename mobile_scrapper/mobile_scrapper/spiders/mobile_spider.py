import scrapy

class MySpider(scrapy.Spider):
  name = "mobile_spider"
  count = 0
  total_pages = 0
  
  def start_requests(self):
        url_to_scrape = input("Flipkart url to scrape: ")
        pages_to_scrape = int(input("Number of pages to scrape: "))
        self.total_pages = pages_to_scrape
        urls = []
        urls.append(url_to_scrape)
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
