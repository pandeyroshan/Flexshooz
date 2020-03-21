from django.contrib import admin

# Register your models here.
from .models import Profile,cart,wishList


admin.site.register(Profile)
admin.site.register(cart)
admin.site.register(wishList)