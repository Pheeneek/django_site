from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)


class Product(models.Model):
    PRODUCT_TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE, null=True)
    price = models.FloatField()
    discount_price = models.IntegerField()
    discount = models.IntegerField()


class Coupon(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together =(('user', 'product'), )
