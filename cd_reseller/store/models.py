from django.db import models

# Create your models here.


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
    price = models.IntegerField(null=False, default=10)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name


