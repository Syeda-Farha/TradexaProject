from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=20)
    weight=models.CharField(max_length=10)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
