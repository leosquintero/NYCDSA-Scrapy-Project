from scrapy import Spider
from trip.items import TripItem
import re

class TirpSpider(Spider):
    name = "trip_spider"
    allowed_urls = 'https://www.tripadvisor.com'
    # Defining the list of pages to scrape
    start_urls = ["https://www.tripadvisor.com/RestaurantSearch-g60763-oa" + str(30*i) + "-a_geobroaden.true-New_York_City_New_York.html#EATERY_LIST_CONTENTS" for i in range(0, 465)]
                   

    def parse(self, response):
        # Defining the rows to be scraped 
        rows = response.xpath("//div[@id='EATERY_SEARCH_RESULTS']/div[@data-index]")
         

        for row in rows: 
            # Extracting restaurant names
            name = row.xpath("./div[2]/div[1]/div[@class='title']/a/text()").extract_first()
            name = name[1:][:-1]

            # Extracting Average rate
            avg = row.xpath(".//div[@class='rating rebrand']/span[1]/@alt").extract_first()
            avg = avg[0:][:-12]
            
            # Extracting price range
            price = row.xpath(".//span[@class='item price']/text()").extract_first()
            
            # Restaurant's rank
            rank = row.xpath(".//div[@class='popIndex rebrand popIndexDefault']/text()").extract_first()
            rank = rank[1:][:-1]
            
            # Scraping cuisine
            cuisine = row.xpath(".//div[2]/div[1]/div[@class='cuisines']/*[@class='item cuisine']/text()").extract()
            

            # Extracting number of reviews
            reviews = row.xpath("./div[2]/div[1]/div[@class='rating rebrand']/span[2]/a/text()").extract_first()
            reviews = reviews[1:][:-9]

            
            
            item = TripItem()
            item['name'] = name
            item['reviews'] = reviews
            item['avg'] = avg
            item['price'] = price
            item['rank'] = rank
            item['cuisine'] = cuisine

            yield item