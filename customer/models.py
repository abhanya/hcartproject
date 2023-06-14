from django.db import models
from seller.models import Product
from hcart.models import Customer,Seller

# Create your models here.

class Cart(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    cust = models.ForeignKey(Customer,on_delete = models.CASCADE)
    prod_quantity = models.IntegerField(default = "1")

class Wishlist(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    cust = models.ForeignKey(Customer,on_delete = models.CASCADE)
    
class Oreder(models.Model):
    cust = models.ForeignKey(Customer,on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    total_price = models.IntegerField()
    payment_mode = models.CharField(max_length=100,null=False)
    tracking_no = models.CharField(max_length=50,null=True)
    created_at = models.DateField(auto_now_add=True)

class Order_item(models.Model):
    oreder = models.ForeignKey(Oreder,on_delete = models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    status= models.CharField(max_length=100,default="pending")

