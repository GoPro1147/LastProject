from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ReviewForm
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
    form = ReviewForm
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'movie_review/detail.html', context)


def actor_detail(request, id):
    actor = get_object_or_404(Actor, id=id)
    context = {
        'actor': actor
    }
    return render(request, 'movie_review/actor_detail.html', context)


@require_POST
@login_required
def create_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movie_review:movie_detail', id)
        

@login_required
def like(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user

    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)

    return redirect('movie_review:movie_detail', id)