from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=30)
    address = models.CharField(max_length=50,default = '')
    gender = models.CharField(max_length=50)
    cust_phone = models.BigIntegerField()
    cust_pass = models.CharField(max_length=8)
    cust_pic = models.ImageField(upload_to='customer/',default= 'customer/profil.webp')

class Seller(models.Model):
    seller_name =models.CharField(max_length=20)
    seller_add =models.CharField(max_length=50)
    seller_gen =models.CharField(max_length=20)
    seller_pho =models.BigIntegerField()
    comp_name =models.CharField(max_length=50)
    acc_hold =models.CharField(max_length=20)
    ifsc =models.CharField(max_length=20)
    branch =models.CharField(max_length=20)
    acc_num =models.BigIntegerField()
    email =models.CharField(max_length=50)
    seller_usr =models.CharField(max_length=30)
    seller_pass =models.CharField(max_length=20)
    seller_pic =models.ImageField(upload_to='seller/')
    approved =models.BooleanField(default=False)