from turtle import color
from django.db import models

# Create your models here.

class ASeries(models.Model):
    id_name=models.IntegerField(blank=True,verbose_name=('id'))
    name=models.CharField(max_length=100,verbose_name=('model name'))
    color=models.CharField(max_length=50,verbose_name=('color'))

class QSeries(models.Model):
    id_name=models.IntegerField(blank=True,verbose_name=('id'))
    name=models.CharField(max_length=100,verbose_name=('model name'))
    color=models.CharField(max_length=50,verbose_name=('color'))       

class ESeries(models.Model):
    id_name=models.IntegerField(blank=True,verbose_name=('id'))
    name=models.CharField(max_length=100,verbose_name=('model name'))
    color=models.CharField(max_length=50,verbose_name=('color'))       


    def __str__(self):
        return self.name
