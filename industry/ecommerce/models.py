from django.db import models

# Create your models here.
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.conf import settings


class Category(models.Model):
    
    category_name =  models.CharField(max_length=200,unique=True)


    # def __str__(self):
    #     return self.category_name


class Product(models.Model):
    
    product_name =  models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,null=True, related_name ="cat_name" , blank=True, on_delete=models.SET_NULL)
    ###############################late
    
    def __str__(self):
    	return self.product_name
