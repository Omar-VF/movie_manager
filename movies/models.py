from django.db import models

# Create your models here.


class censor_info(models.Model):
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.rating


class director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class actors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class movie_data(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField(blank=True)
    poster = models.ImageField(
        upload_to="images/", null=True, blank=True, default="UnavailableImg.png"
    )
    censor_details = models.ForeignKey(
        censor_info,
        on_delete=models.SET_NULL,
        related_name="movie",
        null=True,
        blank=True,
    )

    directed_by = models.ForeignKey(
        director, null=True, on_delete=models.CASCADE, related_name="directed_by", blank=True
    )

    actor = models.ManyToManyField(actors, related_name="acted_movies",blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("title",)
