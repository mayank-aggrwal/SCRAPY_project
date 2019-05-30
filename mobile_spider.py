
import scrapy

class MySpider(scrapy.Spider):

    name = "mobile_spider"
    cnt = 0
    
    def start_requests(self):
        urls = [
            "https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1",
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):

        boxes = response.css("div._1UoZlX")
        for box in boxes:
            mobile_name = box.css("div._3wU53n::text").get()
            mobile_price = box.css("div._1vC4OE._2rQ-NK::text").get()[1:]
            mobile_rating = box.css("div.hGSR34::text").get()

            yield {
                "name":mobile_name,
                "price":mobile_price,
                "rating":mobile_rating,
            }
            
        self.cnt = self.cnt + 1
        self.log(self.cnt)

        pages = response.css("a._3fVaIS::attr(href)").getall()
        next_page_id = pages[0]
        if len(pages) > 1:
            next_page_id = pages[1]
            self.log(next_page_id)

        if self.cnt < 5:
            if next_page_id is not None:
                next_page = response.urljoin(next_page_id)
                self.log(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
