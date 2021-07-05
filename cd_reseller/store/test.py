from store.models import Variety, Price
import random
## I MADE REQUESTS FOR DJANGO SHELL
bad_quality_price = Price.objects.create(price=7)
basic_price = Price.objects.create(price=10)
premium_price = Price.objects.create(price=15)
californian_price = Price.objects.create(price=25)


candies = []
urls = []

for candy in candies:
    data = Variety.objects.create(reference=n, title=candy, picture=urls[n])
    data.prices.add(random.choice([bad_quality_price, basic_price, premium_price, californian_price]))
    n+=1
    

    

    