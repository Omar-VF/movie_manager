from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(movie_data)
admin.site.register(director)
admin.site.register(censor_info)
admin.site.register(actors)