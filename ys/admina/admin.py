#-*- coding: utf-8-*-
from django.contrib import admin

# Register your models here.

from admina import models

admin.site.register(models.Image)
admin.site.register(models.Column)
admin.site.register(models.Department)
admin.site.register(models.News)
admin.site.register(models.Administrators)