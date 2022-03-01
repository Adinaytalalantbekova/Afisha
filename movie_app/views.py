from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import MovieSerializer, DirectorSerializer, MovieCreateUpdateSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status
from . import serializers


@api_view(['GET', 'POST'])
def director(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            name = request.data.get('name')
            director = Director.objects.create(name=name)
            return Response(data=DirectorSerializer(director).data,
                            status=status.HTTP_201_CREATED)


@property
def reviews_count(self):
    return self.reviews.all().count()


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    if request.method == 'GET':
        data = MovieSerializer(directors).data
        return Response(data=data)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            directors.name = request.data.get('name')
            directors.seve()
            return Response(data=MovieSerializer(directors).data)


@api_view(['GET', 'POST'])
def movie(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True)
        return Response(data=data)
    elif request.method == 'POST':
        serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            title = request.data.get('title')
            description = request.data.get('description')
            duration = request.data.get('duration')
            director = request.data.get('director')
            movies = Movie.objects.create(title=title, description=description,
                                          duration=duration, director_id=director)
            return Response(data=MovieSerializer(movies).data,
                            status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found'})
    if request.method == 'GET':
        data = MovieSerializer(movies).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            movies.title = request.data.get('title')
            movies.description = request.data.get('description')
            movies.duration = request.data.get('duration')
            movies.director = request.data.get('director')
            movies.seve()
            return Response(data=MovieSerializer(movies).data)


@api_view(['GET', 'POST'])
def review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = MovieSerializer(reviews, many=True)
        return Response(data=data)
    elif request.method == 'POST':
        serializer = serializers.ReviewCreateSerialiser(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            text = request.data.get('text')
            stars = request.data.get('stars')
            reviews = Review.objects.create(text=text, stars=stars)
            return Response(data=ReviewSerializer(reviews).data,
                            status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'POST'])
def review_detail(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found'})
    if request.method == 'GET':
        data = MovieSerializer(reviews).data
        return Response(data=data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = serializers.ReviewCreateSerialiser(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            reviews.stars = request.data.get('stars')
            reviews.text = request.data.get('text')
            reviews.movie = request.data.get('movie')
            reviews.seve()
            return Response(data=MovieSerializer(reviews).data)


