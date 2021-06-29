from django.db import models

# Create your models here.


PRICES = {
    'amnesia-haze' : {'price' : "10"},
    'critical-2.0': {'price' : "15" },
    'lemon-haze' : {'price' : "8" },
}

VARIETIES = [
    {'name' : 'Amnesia Haze', 'prices' : [PRICES['amnesia-haze']]},
    {'name' : 'Critical 2.0 + ', 'prices' : [PRICES['critical-2.0']]},
    {'name' : 'Lemon Haze', 'prices' : [PRICES['lemon-haze']]},
]

class Price(models.Model):
    price = models.IntegerField(max_length=5)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)


class Variety(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    picture = models.URLField()
    prices = models.ManyToManyField(Price, related_name='varieties', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    variety = models.OneToOneField(Variety)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


