# Generated by Django 4.1 on 2022-09-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samsung', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.IntegerField(blank=True, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='model name')),
                ('color', models.CharField(max_length=50, verbose_name='color')),
            ],
        ),
    ]
