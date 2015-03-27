from django.contrib import admin
from django.db import models

# Create your models here.
from django.db import models

class Order(models.Model):
    image = models.ImageField()
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    paid = models.BooleanField(default=False)

admin.site.register(Order)