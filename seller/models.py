from django.db import models
from hcart.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE,default="")
    product_name = models.CharField(max_length=200)
    product_details = models.CharField(max_length=500)
    product_number = models.BigIntegerField()
    current_stock = models.IntegerField()
    product_image = models.ImageField(upload_to="product")
    product_price = models.FloatField()
    product_category = models.CharField(max_length=100,default="")
    product_place = models.CharField(max_length=100,default="")
