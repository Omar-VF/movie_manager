from django.db import models

# Create your models here.

class movie_data(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    summary=models.TextField(blank=True)

class Director(models.Model):
    name=models.CharField(max_length=300)