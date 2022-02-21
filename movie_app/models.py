from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 related_name='reviews')

    def __str__(self):
        return self.title


    @property
    def rating(self):
        return Review.objects.filter(movie=self).aggregate(Avg('stars'))


class Review(models.Model):
    stars = models.IntegerField(default=5)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title





