from django.db import models
from management.models import University
from django.contrib.auth.models import User
from store.models import Product

# Create your models here


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.CharField("First Name",max_length=100,blank=True)
    lname = models.CharField("Last Name",max_length=100,blank=True)
    contact_number = models.CharField("Contact Number",max_length=15,blank=True)
    address = models.CharField("Address",max_length=200,blank=True)
    email = models.EmailField("Email",max_length=100,blank=True)
    university = models.ForeignKey(University,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'User Profiles'
        verbose_name_plural = 'User Profiles'

class cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    productID = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.user.username+' Cart'
    
    class Meta:
        verbose_name = 'Carts'
        verbose_name_plural = 'Carts'

class wishList(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    productID = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.user.username+' Wishlist'
    
    class Meta:
        verbose_name = 'Wishlists'
        verbose_name_plural = 'Wishlists'