from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

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

    def rating(self):
        count_reviews = self.reviews.count()
        sum = self.reviews.aggregate(Sum('rate'))['rate__sum']
        try:
            return sum / count_reviews
        except:
            return 0



class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)

    def __str__(self):
        return self.movie.title





