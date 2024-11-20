import scrapy
from ..items import JumiascraperItem


class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/ios-phones/"]

    def parse(self, response):
        
        body = response.css(".core")

        for card in body:
            # Ensures the product is not out of stock
            tag = card.css("._xs::text").get()
            if tag:
                if "stock" not in card.css("._xs::text").get():
                    product_link = card.css("a::attr(href)").get()
                    yield response.follow(url=product_link, callback=self.get_data)
            else:
                product_link = card.css("a::attr(href)").get()
                yield response.follow(url=product_link, callback=self.get_data)

        # Gets the link for the next page and follows it
        next_page = response.css(".pg:nth-child(6)::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback= self.parse)

    def get_data(self, response):
        # initialize item class 
        items = JumiascraperItem()

        # Extract data
        phone_name = response.css(".-fs20.-pbxs::text").get()
        # phone_model = self.extract_model(phone_name)
        phone_price = response.css(".-fs24::text").get()
        units_left = response.css(".-rd5::text").get()
        delivery_type = response.css(".-fw .ic::attr(aria-label)").get()
        verified_ratings = response.css(".-plxs._more::text").get()
        seller_name = response.css(".-hr.-pas .-pbs::text").get()
        seller_score = response.css(".-m.-prxs::text").get()
        seller_followers = response.css(".-prs span.-m::text").get()
        seller_shipping_speed = response.css(".-fs14+ .-pts .-m::text").get()
        seller_quality_score = response.css(".-i-ctr:nth-child(3) .-m::text").get()
        seller_customer_rating = response.css(".-pts~ .-pts+ .-pts .-m::text").get()

        items['phone_name'] = phone_name
        items['phone_price'] = phone_price
        items['units_left'] = units_left
        items['delivery_type'] = delivery_type
        items['verified_ratings'] = verified_ratings
        items['seller_name'] = seller_name
        items['seller_score'] = seller_score
        items['seller_followers'] = seller_followers
        items['seller_shipping_speed'] = seller_shipping_speed
        items['seller_quality_score'] = seller_quality_score
        items['seller_customer_rating'] = seller_customer_rating

        yield items