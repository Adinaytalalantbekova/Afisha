from rest_framework import serializers
from movie_app.models import Director, Review, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration rating'.split()

