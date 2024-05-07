from django.db import models

# Create your models here.

class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=1000)
    item_price = models.IntegerField(null=False)
    item_photo = models.FileField(upload_to='media/photo',default='0')

class Order(models.Model):
    pass