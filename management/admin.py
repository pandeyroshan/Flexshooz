from django.contrib import admin

# Register your models here.
from .models import University,representative,consignment,representativePush,newsletters

admin.site.register(University)
admin.site.register(representative)
admin.site.register(consignment)
admin.site.register(representativePush)
admin.site.register(newsletters)