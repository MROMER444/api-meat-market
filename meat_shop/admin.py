from django.contrib import admin
from meat_shop.models import *


class Config(admin.ModelAdmin):
    admin.site.register(Product)
    admin.site.register(Favorite)
    admin.site.register(Profile)
    admin.site.register(Cart)
    admin.site.register(Order)