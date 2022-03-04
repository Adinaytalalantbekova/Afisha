from rest_framework import serializers
from movie_app.models import Director, Review, Movie
from . import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration rating'.split()

    def get_category(self, movie_app):
        try:
            return movie_app.category.name
        except:
            return "No category"

    def get_reviews(self, movie_app):
        serialiser = ReviewSerializer(Review.objects.filter(author__isnull=False,
                                                            product=movie_app), many=True)
        return serialiser.data

    def validate_director_id(self, attrs):
        if models.Director.objects.filter(id=attrs).count == 0:
            raise ValidationError(f'message:{attrs} not found')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerialiser(serializers.Serializer):
    stars = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField()

    def validate_movie_id(self, movie_id):
        if models.Movie.objects.filter(id=movie_id).count == 0:
            raise ValidationError(f'message: movie id not found')


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.CharField(max_length=10)

    def validate_movie(self, movies):
        if Movie.objects.filter(id=movies).count()==0:
            raise ValidationError(f'Movie with id={movies} not found')
        return movies


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate_username(self,username):
        if User.objects.filter(username=username):
            raise ValidationError('user with this username is already exists')
        return username




class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_token(self,token):
        if User.objects.filter(token=token):
            raise ValidationError('this user is already logged in')

