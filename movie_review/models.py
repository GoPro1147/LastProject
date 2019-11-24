from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genreNm = models.CharField(max_length=100)

    def __str__(self):
        return self.genreNm

class Actor(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=300)
    openDt = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.ManyToManyField(Actor, related_name='filmography')
    mvdirector = models.CharField(max_length=100, blank=True)
    img_url = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    

    def __str__(self):
        return self.title

    
class Review(models.Model):
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
