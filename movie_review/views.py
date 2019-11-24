from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Actor
# Create your views here.

def index(request):
    return render(request, 'movie_review/index.html')


def movie_select(request):
    movie_list = Movie.objects.all()
    context = {
        'movie_list': movie_list
    }
    return render(request, 'movie_review/list.html', context)


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_review/detail.html', context)


def actor_detail(request, id):
    actor = get_object_or_404(Actor, id=id)
    context = {
        'actor': actor
    }
    return render(request, 'movie_review/actor_detail.html', context)