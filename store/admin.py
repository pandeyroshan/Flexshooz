from django.contrib import admin

# Register your models here.

from .models import shoe_size,shoe_color,category,Product,CheckOut

admin.site.register(shoe_size)
admin.site.register(shoe_color)
admin.site.register(category)
admin.site.register(Product)
admin.site.register(CheckOut)