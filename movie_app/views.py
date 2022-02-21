from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import MovieSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def director(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = MovieSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        return Response(data={'massage': 'Data Received!'})


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
        directors.name = request.data.get('name')
        directors.seve()
        return Response(data=MovieSerializer(directors).data)



@api_view(['GET'])
def movie(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True)
    return Response(data=data)


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
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.duration = request.data.get('duration')
        movies.director = request.data.get('director')
        movies.seve()
        return Response(data=MovieSerializer(movies).data)



@api_view(['GET'])
def review(request):
    reviews = Review.objects.all()
    data = MovieSerializer(reviews, many=True)
    return Response(data=data)


@api_view(['GET'])
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
        reviews.stars = request.data.get('stars')
        reviews.text = request.data.get('text')
        reviews.movie = request.data.get('movie')
        reviews.seve()
        return Response(data=MovieSerializer(reviews).data)


