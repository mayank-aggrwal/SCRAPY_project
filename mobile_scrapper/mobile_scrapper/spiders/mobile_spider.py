import scrapy

class MySpider(scrapy.Spider):
  name = "mobile_spider"
  count = 0
  total_pages = 0
