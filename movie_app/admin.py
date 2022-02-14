from django.contrib import admin
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
