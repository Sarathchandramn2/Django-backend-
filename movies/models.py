from django.db import models

# Create your models here.

class movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    MovieName = models.CharField(max_length=100)
    MovieGenre=models.CharField(max_length=100)
    Director=models.CharField(max_length=100)
    Language=models.CharField(max_length=100)