from django.urls import path
from . import views

app_name="movie_review"

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_select, name="movie_select"),
    path('movie/<int:id>/', views.movie_detail, name="movie_detail"),
    path('actor/<int:id>/', views.actor_detail, name="actor_detail"),
    
]