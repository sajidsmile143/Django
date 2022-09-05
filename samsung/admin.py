from turtle import color
from django.contrib import admin
from .models import *
# Register your models here.

# @admin.ASeriesAdmin(admin.ModelAdmin)
# class Aseries(models.Model):
#     list_display=['id','name','color' ,]

# @admin.register(admin.ModelAdmin)
# class ASeries(models.Model):
#     list_display=['id_name','name','color' ,]

admin.site.register(ASeries)
admin.site.register(QSeries)
admin.site.register(ESeries)
    