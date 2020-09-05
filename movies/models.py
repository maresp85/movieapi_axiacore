from django.db import models


''' Genres Model '''
class Genre(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)


''' Movie Model '''
class Movie(models.Model):

    overview = models.CharField(max_length=800, null=False)
    poster_path = models.CharField(max_length=100, null=False)
    original_title = models.CharField(max_length=100, null=False)
    original_language = models.CharField(max_length=4, null=False)
    title = models.CharField(max_length=60, null=False)
    release_date = models.DateField(null=False)
    rating = models.DecimalField(default=5, max_digits=2, decimal_places=1)
    genre_id = models.ManyToManyField(Genre)
