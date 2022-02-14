from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import MovieAppSerializer
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from rest_framework import status

@api_view(['GET'])
def director(request):
    directors = Director.objects.all()
    data = MovieAppSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    data = MovieAppSerializer(directors).data
    return Response(data=data)



@api_view(['GET'])
def movie(request):
    movies = Movie.objects.all()
    data = MovieAppSerializer(movies, many=True)
    return Response(data=data)


@api_view(['GET'])
def movie_detail(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found'})
    data = MovieAppSerializer(movies).data
    return Response(data=data)


@api_view(['GET'])
def review(request):
    reviews = Review.objects.all()
    data = MovieAppSerializer(reviews, many=True)
    return Response(data=data)

@api_view(['GET'])
def review_detail(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found'})
    data = MovieAppSerializer(reviews).data
    return Response(data=data)

