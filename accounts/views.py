from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from movie_review.models import Movie, Review, Genre

# Create your views here.


def signup(request):
    if request.method == "POST":
            signup_form = UserCustomCreationForm(request.POST)
            login_form = AuthenticationForm()
            if signup_form.is_valid():
                signup_form.save()
                return redirect('movie_review:index')
    else:
        form = UserCustomCreationForm()

    context={
        'signup_form':signup_form,
        'login_form':login_form
    }
    return redirect('movie_review:index')


def login(request):
    movie_list = Movie.objects.all()
    user_model = get_user_model()
    user_list = user_model.objects.all()
    signup_form = UserCustomCreationForm()
    context = {
        'movie_list': movie_list,
        'user_list': user_list,
        'signup_form': signup_form
    }
    if request.user.is_superuser:
        return render(request, 'accounts/admin.html', context)
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if form.get_user().is_superuser:
                return render(request, 'accounts/admin.html', context)
            return redirect('movie_review:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'accounts/form.html',context)


def logout(request):
    auth_logout(request)
    return redirect('movie_review:index')


def user_info(request, id):
    
    genres = Genre.objects.all()
    user_model = get_user_model()
    user_p = get_object_or_404(user_model, id=id)
    
    genre_box = [[0, 0] for _ in range(19)]
    
    for i in range(19):
        genre_box[i][1] = i
    user_like_movie = user_p.like_movies.all()
    for movie in user_like_movie:
        for genre in movie.genres.all():
            genre_box[genre.id][0] += 1
    
    genre_box.sort(key= lambda x: x[0], reverse=True)
    recommend = [0] * 3
    cnt = 0
    for i in range(19):
        sel_gen = genre_box[i][1]
        for movie in genres[sel_gen].genre_movies.all():
            if movie in user_like_movie:
                continue
            else:
                recommend[cnt] = movie
                cnt += 1
            if cnt == 3:
                break
        else:
            continue
        break
    print(recommend)   
    
    context = {
        'user_p':user_p,
        'recommend':recommend,
        'like_Genre': get_object_or_404(Genre, id=sel_gen)
    }
    return render(request, 'accounts/user_info.html', context)

@require_POST
def user_delete(request, id):
    movie_list = Movie.objects.all()
    user_model = get_user_model()
    user_list = user_model.objects.all()
    context = {
        'movie_list': movie_list,
        'user_list': user_list
    }

    if request.user.is_superuser:
        user_info = get_object_or_404(user_model, id=id)
        user_info.delete()

    return render(request, 'accounts/admin.html', context)

