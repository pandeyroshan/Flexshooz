from django.db import models
from django.contrib.auth.models import User
from management.models import University
# Create your models here.


class shoe_size(models.Model):
    number = models.IntegerField('Shoe Number', blank=False,default=8)

    def __str__(self):
        return str(self.number)
    
    class Meta:
        verbose_name = 'Shoe Numbers'
        verbose_name_plural = 'Shoe Numbers'

class shoe_color(models.Model):
    color = models.CharField('Colors',max_length=20,blank=False)

    def __str__(self):
        return self.color
    
    class Meta:
        verbose_name = 'Colors'
        verbose_name_plural = 'Colors'

class category(models.Model):
    name = models.CharField('Category',max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class Product(models.Model):
    name = models.CharField('Name',max_length=200)
    tagline = models.CharField('Tagline',max_length=300)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    shoe_color = models.ForeignKey(shoe_color,on_delete=models.CASCADE)
    shoe_size = models.ManyToManyField(shoe_size,related_name='sizeofshoe')
    description = models.TextField()
    product_code = models.CharField(max_length=15)
    price = models.IntegerField('Price',default=1200)
    fake_price = models.IntegerField('Fake Price',default=1200)
    img1 = models.ImageField('Image 1', upload_to='Product Images')
    img2 = models.ImageField('Image 2', upload_to='Product Images',blank=True)
    img3 = models.ImageField('Image 3', upload_to='Product Images',blank=True)
    img4 = models.ImageField('Image 4', upload_to='Product Images',blank=True)

    def __str__(self):
        return self.product_code
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

class CheckOut(models.Model):
    Product = models.ManyToManyField(Product,related_name='shoes')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    University = models.ForeignKey(University,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user+' checkout '+self.University
    
    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkout'