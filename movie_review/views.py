from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ReviewForm, MovieForm
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCustomCreationForm
from .models import Movie, Actor, Review, Genre
from django.http import JsonResponse
# Create your views here.


def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCustomCreationForm()
    context = {
        "login_form": login_form,
        "signup_form": signup_form,
    }
    return render(request, 'movie_review/index.html', context)


def movie_select(request, id):
    if id == 0:
        movie_list = Movie.objects.all()
    else:
        movie_list = Movie.objects.filter(genres__id=id)
    genre_list = Genre.objects.all()
    login_form = AuthenticationForm()
    signup_form = UserCustomCreationForm()
    
    context = {
        'movie_list': movie_list,
        'genres': genre_list,
        'gen_id': genre_list[id],
        'login_form': login_form,
        'signup_form': signup_form,
    }
    return render(request, 'movie_review/list.html', context)


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = ReviewForm()
    login_form = AuthenticationForm()
    signup_form = UserCustomCreationForm()
    all_rating = 0
    if movie.review_set.count():
        for review in movie.review_set.all():
            all_rating += review.rating
        
        avg_rating = all_rating / movie.review_set.count()
    else:
        avg_rating = '평가가 없습니다.'
    
    context = {
        'movie': movie,
        'form': form,
        'login_form': login_form,
        'signup_form': signup_form,
        'avg_rating': avg_rating,
    }
    return render(request, 'movie_review/detail.html', context)


def actor_detail(request, id):
    actor = get_object_or_404(Actor, id=id)
    login_form = AuthenticationForm()
    signup_form = UserCustomCreationForm()
    context = {
        'actor': actor,
        'login_form': login_form,
        'signup_form': signup_form,
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


@require_POST
@login_required
def delete_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user or request.user.is_superuser:
        review.delete()
    return redirect('accounts:user_info', request.user.id)


@login_required
def update_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user.is_superuser:
        review.content = "관리자에 의해 제한된 한줄평 입니다."
        review.save()
        return redirect('movie_review:movie_detail', movie_id)
    if review.user == request.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save()
            return redirect('movie_review:movie_detail', movie_id)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            'form': review_form
        }
        return render(request, 'movie_review/form.html', context)
    else:
        return redirect('movie_review:movie_detail', movie_id)
        

@login_required
@require_POST
def like(request, id):
    if request.is_ajax():
        movie = get_object_or_404(Movie, id=id)
        user = request.user

        if user in movie.like_users.all():
            movie.like_users.remove(user)
            is_like = False
        else:
            movie.like_users.add(user)
            is_like = True

        context = {
            'is_like': is_like,
            'like_count': movie.like_users.all().count()
        }
        return JsonResponse(context)
    else:
        return JsonResponse({'message': '잘못된 요청입니다.'})


@login_required
def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.user.is_superuser:
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie = form.save()
            return redirect('movie_review:movie_detail', id)

        else:
            form = MovieForm(instance=movie)
        context = {
            'form': form
        }
        return render(request, 'movie_review/form.html', context)
    else:
        return redirect('movie_review:movie_detail', id)


@login_required
@require_POST
def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.user.is_superuser:
        movie.delete()

    return redirect('movie_review:movie_select', 0)


def search(request):
    keyword = request.GET.get('keyword')
    movies = Movie.objects.filter(title__contains=keyword)
    actors = Actor.objects.filter(name__contains=keyword)
    genre_list = Genre.objects.all()
    login_form = AuthenticationForm()
    signup_form = UserCustomCreationForm()
    if not movies:
        movies = ""
    if not actors:
        actors = ""
    context = {
        'movie_list': movies,
        'actor_list': actors,
        'genres': genre_list,
        'gen_id': genre_list[0],
        'login_form': login_form,
        'signup_form': signup_form,
    }
    return render(request, 'movie_review/search_result.html', context)
    

def show(request, id):
    if request.is_ajax():
        movie = get_object_or_404(Movie, id=id)
        all_rating = 0
        if movie.review_set.count():
            for review in movie.review_set.all():
                all_rating += review.rating
            
            avg_rating = all_rating / movie.review_set.count()
        else:
            avg_rating = 0
            

        context = {
            'avg_rating': avg_rating,
            'like_count': movie.review_set.count()
        }
        return JsonResponse(context)
    else:
        return JsonResponse({'message': '잘못된 요청입니다.'})
    pass





        