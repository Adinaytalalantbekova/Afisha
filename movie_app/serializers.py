from rest_framework import serializers
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review



class MovieAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'title  description duration '.split()