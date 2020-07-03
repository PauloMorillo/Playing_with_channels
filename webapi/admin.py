from django.contrib import admin

# Register your models here.
from .models import User, Help, Store

models2show = [User, Help, Store]
#@admin.register(User, Help, Store)
admin.site.register(models2show)
