from django.contrib import admin

from .models import Option, Main

admin.site.register(Main)
admin.site.register(Option)