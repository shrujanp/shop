from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()
    Stock = models.IntegerField()
    Image_Url = models.CharField(max_length= 1023)


class Offer(models.Model):
    Code = models.CharField(max_length=2550)
    Description = models.CharField(max_length=255)
    Discount = models.FloatField()
