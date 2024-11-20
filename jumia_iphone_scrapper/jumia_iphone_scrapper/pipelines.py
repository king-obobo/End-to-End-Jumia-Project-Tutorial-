# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class JumiaIphoneScrapperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Lets extract the model name from the phone name
        phone_name = adapter.get("phone_name")
        adapter['phone_name'] = self.extract_model(phone_name)

        # Working on the price
        phone_price = adapter.get('phone_price')
        adapter['phone_price'] = phone_price.replace('₦ ', '').replace(',', '')

        # Working on the ratings
        verified_ratings = adapter.get('verified_ratings')
        adapter['verified_ratings'] = self.extract_rating(verified_ratings)

        # Working on units_left
        units_left = adapter.get("units_left")
        if units_left:
            adapter['units_left'] = units_left
        else:
            adapter['units_left'] = "In stock"

        # Working on delivery_type
        delivery_type = adapter['delivery_type']
        if delivery_type:
            adapter['delivery_type'] = delivery_type
        else:
            adapter['delivery_type'] = "Jumia Nigeria"

        # Working on seller_score
        seller_score = adapter.get('seller_score')
        if '%' in seller_score:
            adapter['seller_score'] = seller_score.replace('%', '')
        else:
            adapter['seller_score'] = 0

        return item

    def extract_model(self, phone_name):
        pattern = re.compile(r'(iPhone\s?(?:\d{1,2}|X|XS|XR|SE)(?:\s?(Pro Max|Pro|Max|Mini)?)?)', re.IGNORECASE)
        if pattern.search(phone_name):
            return pattern.search(phone_name).group(1)
        else:
            return phone_name
    
    def extract_rating(self, verified_ratings):
        try:
            verified_ratings = verified_ratings.strip('()')
            match = re.search(r'\d+', verified_ratings)
            if match:
                return int(match.group())
            else:
                return 0
        except:
            return 0
