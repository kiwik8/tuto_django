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
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Variety(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    picture = models.URLField()
    prices = models.ManyToManyField(Price, related_name='varieties', blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    variety = models.OneToOneField(Variety, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name


