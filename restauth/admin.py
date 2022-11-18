from django.contrib import admin

from .models import EmailAccount


class Config(admin.ModelAdmin):
    admin.site.register(EmailAccount)
