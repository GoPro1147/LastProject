from django.urls import path
from . import views

app_name="movie_review"

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_select, name="movie_select"),
    path('movie/<int:id>/', views.movie_detail, name="movie_detail"),
    path('actor/<int:id>/', views.actor_detail, name="actor_detail"),
    path('<int:id>/create_review/', views.create_review, name="create_review"),
    path('like/<int:id>/', views.like, name="like"),
    
]