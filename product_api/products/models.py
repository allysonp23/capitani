from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    pricing_amount = models.FloatField()
    pricing_currency = models.CharField(max_length=10)
    availability_quantity = models.IntegerField()
    availability_timestamp = models.DateTimeField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
