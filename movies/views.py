from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})
