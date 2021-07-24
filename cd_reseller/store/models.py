from django.db import models

# Create your models here.


class Variety(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    picture = models.URLField()
    price = models.IntegerField(null=False, default=10)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    email = models.EmailField(null=False)
    address = models.CharField(null=False, max_length=400)
    pgp_public_address = models.TextField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.contact.name
