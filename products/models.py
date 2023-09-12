from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
