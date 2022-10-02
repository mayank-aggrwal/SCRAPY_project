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
def extractInfo(boxes):
    	for box in boxes:
            scraped_mobile_name = box.css("div._3wU53n::text").get()
            scraped_mobile_price = box.css("div._1vC4OE._2rQ-NK::text").get()[1:]
            scraped_mobile_rating = box.css("div.hGSR34::text").get()

            yield {
                "mobile":mobile_name,
                "cost":mobile_price,
                "rating":mobile_rating,
            }

    def parse(self, response):
        boxes = response.css("div._1UoZlX")
        extractInfo(boxes)
            
        self.count = self.count + 1
        self.log(self.count)

        pages = response.css("a._3fVaIS::attr(href)").getall()
        next_page_id = pages[0]
        if len(pages) > 1:
            next_page_id = pages[1]
            self.log(next_page_id)

        if self.count < self.total_pages:
            if next_page_id is not None:
                next_page = response.urljoin(next_page_id)
                self.log(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
