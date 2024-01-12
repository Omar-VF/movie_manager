from django.db import models

# Create your models here.

class movie_data(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    summary=models.TextField(blank=True)
    poster=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.title

class Director(models.Model):
    name=models.CharField(max_length=300)