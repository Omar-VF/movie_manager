from django.contrib import admin
from . models import movie_data,Director
# Register your models here.

admin.site.register(movie_data)
admin.site.register(Director)