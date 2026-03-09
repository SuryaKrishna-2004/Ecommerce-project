from django.db import models

# model for product

class Product(models.Models):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField()
    