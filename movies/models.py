from django.db import models

# Create your models here.


class censor_info(models.Model):
    rating = models.CharField(max_length=10)
    
    def __str__(self):
        return self.rating


class movie_data(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField(blank=True)
    poster = models.ImageField(
        upload_to="images/", null=True, blank=True, default="UnavailableImg.png"
    )
    censor_details = models.OneToOneField(
        censor_info, on_delete=models.SET_NULL, related_name="movie", null=True, blank=True
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ("title",)


class Director(models.Model):
    name = models.CharField(max_length=300)
