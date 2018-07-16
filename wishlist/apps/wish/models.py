from django.db import models
from ..login.models import User

class ProductManager(models.Manager):
    pass

class Product(models.Model):
    product_name = models.CharField(max_length = 255)
    creator = models.ForeignKey(User, related_name = 'created_product')
    wanters = models.ManyToManyField(User, related_name = 'wanted')
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    objects = ProductManager()


# Create your models here.
